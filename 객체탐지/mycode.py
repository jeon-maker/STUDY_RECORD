import torch.nn as nn
import torch.utils.data as data
import torch
import cv2
import numpy as np
import os.path as osp
from torchsummary import summary

# xml 파일이나 텍스트를 읽고 가공 및 저장하는 라이브러리
import xml.etree.ElementTree as ET

from data_augumentation import Compose, ConvertFromInts, ToAbsoluteCoords, PhotometricDistort, Expand, RandomSampleCrop, RandomMirror, ToPercentCoords, Resize, SubtractMeans

def make_datapath_list(rootpath):
    imgpath_template = osp.join(rootpath, 'JPEGImages', '%s.jpg')
    annopath_template = osp.join(rootpath, 'Annotations', '%s.xml')
    
    train_id_names = osp.join(rootpath + 'ImageSets/Main/train.txt')
    val_id_names = osp.join(rootpath + 'ImageSets/Main/val.txt')
    
    train_img_list = list()
    train_anno_list = list()
    
    for line in open(train_id_names):
        file_id = line.strip()
        img_path = (imgpath_template % file_id)
        anno_path = (annopath_template % file_id)
        train_img_list.append(img_path)
        train_anno_list.append(anno_path)
        
    val_img_list = list()
    val_anno_list = list()
    
    for line in open(val_id_names):
        file_id = line.strip()
        img_path = (imgpath_template % file_id)
        anno_path = (annopath_template % file_id)
        val_img_list.append(img_path)
        val_anno_list.append(anno_path)
        
    return train_img_list, train_anno_list, val_img_list, val_anno_list
class Anno_xml2list(object):
    def __init__(self, classes):
        self.classes = classes
        
    def __call__(self, xml_path, width, height):
        # xml_path : xml 파일의 경로
        # width : 대상 이미지의 폭
        # height : 대상 이미지의 높이
        # return : [[xmin, ymin, xmax, ymax, label_idx], ... ]
        # 물체의 어노테이션 데이터를 저장한 리스트 / 이미지에 존재하는 물체수만큼의 요소 가짐
        ret = []
        # xml파일 로드
        xml = ET.parse(xml_path).getroot()
        
        # 이미지 내에 있는 물체의 수만큼 반복
        for obj in xml.iter('object'):
            # 어노테이션에서 감지가 difficult로 설정된 것은 제외
            difficult = int(obj.find('difficult').text)
            if difficult == 1:
                continue
            
            # 한 물체의 어노테이션을 저장하는 리스트
            bndbox = []
            
            name = obj.find('name').text.lower().strip()
            bbox = obj.find('bndbox')
            # 어노테이션의 xmin, ymin, xmax, ymax 취득하고 0~1로 규격화
            pts = ['xmin', 'ymin', 'xmax', 'ymax']
            
            for pt in (pts):
                # VOC는 원점이 (1,1)이므로 1을 빼서 (0,0)으로 함
                cur_pixel = int(bbox.find(pt).text) - 1
                
                # 폭, 높이로 규격화
                if pt == 'xmin' or pt == 'xmax':
                    cur_pixel /= width
                else:
                    cur_pixel /= height
                    
                bndbox.append(cur_pixel)
                
            # 어노테이션의 클래스명 index를 취득하여 추가
            label_idx = self.classes.index(name)
            bndbox.append(label_idx)
            
            ret += [bndbox]
        
        return np.array(ret)
class DataTransform():
    # input_size : resize할 이미지 크기
    # color_mean : (B, G, R) 각 색상 채널의 평균값
    def __init__(self, input_size, color_mean):
        self.data_transform = {
            'train': Compose([
                ConvertFromInts(), # int를 float32로 변환
                ToAbsoluteCoords(), # 어노테이션 데이터의 규격화를 반환
                PhotometricDistort(), # 이미지의 색조 등을 임의로 변화시킴
                Expand(color_mean), # 이미지의 캔버스를 확대
                RandomSampleCrop(), # 이미지 내의 특정 부분을 무작위로 추출
                RandomMirror(), # 이미지를 반전
                ToPercentCoords(), # 어노테이션 데이터를 0~1로 규격화
                Resize(input_size), # 이미지 크기를 input_size x input_size로 변형
                SubtractMeans(color_mean) # BGR 색상의 평균값을 뺌
            ]),
            'val': Compose([
                ConvertFromInts(),
                Resize(input_size),
                SubtractMeans(color_mean)
            ])
        }
        
    def __call__(self, img, phase, boxes, labels):
        # phase : 'train' or 'val' 전처리 모드 지정
        return self.data_transform[phase](img, boxes, labels)
# VOC2012의 Dataset을 만드는 클래스 (pytorch의 dataset 클래스 상속받음)    
class VOCDataset(data.Dataset):
    def __init__(self, img_list, anno_list, phase, transform, transform_anno):
        self.img_list = img_list
        self.anno_list = anno_list
        self.phase = phase
        self.transform = transform
        self.transform_anno = transform_anno
        
    def __len__(self):
        # 이미지 매수를 반환
        return len(self.img_list)

    def __getitem__(self, index):
        # 전처리한 이미지의 텐서 형식 데이터와 어노테이션을 반환
        img, gt, h, w = self.pull_item(index)
        return img, gt
    
    def pull_item(self, index):
        # 전처리한 이미지의 텐서 형식 데이터, 어노테이션, 이미지 높이, 폭을 반환
        
        # 1. 이미지 읽기
        img_file_path = self.img_list[index]
        img = cv2.imread(img_file_path) # [높이][폭][색BGR]
        height, width, channels = img.shape # 이미지 크기 취득
        
        # 2. xml 형식의 어노테이션 정보를 리스트에 저장
        anno_file_path = self.anno_list[index]
        anno_list = self.transform_anno(anno_file_path, width, height)
        
        # 3. 전처리 실시
        img, boxes, labels = self.transform(
            img, self.phase, anno_list[:, :4], anno_list[:, 4])
        
        # 색상 채널 순서가 BGR 이므로 RGB로 순서 변경
        # 또한 (높이, 폭, 색상 채널)의 순서를 (색상 채널, 높이, 폭)으로 변경
        img = torch.from_numpy(img[:, :, (2, 1, 0)]).permute(2, 0, 1)
        
        # BBox와 라벨을 한 세트로 한 np.array를 작성, 변수 이름 'gt'는 ground truth의 약칭
        gt = np.hstack((boxes, np.expand_dims(labels, axis=1)))
        
        return img, gt, height, width
def od_collate_fn(batch):
    # 데이터에서 꺼내는 어노테이션 데이터의 크기가 이미지마다 다름
    # 이미지 내의 물체 수가 2개이면 (2, 5) 크기이지만, 3개이면 (3, 5) 등으로 바뀜
    # 미니 배치 분량의 이미지가 나열된 리스트 변수 batch에 미니 배치 번호를 지정하는 차원을 
    # 맨 앞에 하나 추가해서 리스트의 형태를 변형함
    targets = []
    imgs = []
    for sample in batch:
        imgs.append(sample[0])
        targets.append(torch.FloatTensor(sample[1]))
        
    # imgs는 미니 배치 크기의 리스트
    # 리스트 요소가 torch.Size([3, 300, 300])라면,
    # 이 리스트를 torch.Size([batch_num, 3, 300, 300])의 텐서로 변환
    imgs = torch.stack(imgs, dim=0)
    
    # targets는 어노테이션의 정답인 gt의 리스트
    # 리스트 크기는 미니 배치의 크기
    # targets 리스트의 요소는 [n, 5]로 되어있음
    # n은 이미지 속 물체의 수로 이미지마다 다름
    # 5는 [xmin, ymin, xmax, ymax, class_index]임
    
    return imgs, targets
import torch
import torch.nn as nn

class ResidualBlock(nn.Module):
    def __init__(self, in_channels, mid_channels, out_channels, downsample=False):
        super(ResidualBlock, self).__init__()

        self.conv1 = nn.Conv2d(in_channels, mid_channels, kernel_size=1, stride=1, bias=False)
        self.bn1 = nn.BatchNorm2d(mid_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(mid_channels, mid_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(mid_channels)
        self.conv3 = nn.Conv2d(mid_channels, out_channels, kernel_size=1, stride=1, bias=False)
        self.bn3 = nn.BatchNorm2d(out_channels)

        self.downsample = downsample
        if self.downsample:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=2, bias=False),
                nn.BatchNorm2d(out_channels)
            )
        else:
            self.shortcut = nn.Sequential()

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)

        if self.downsample:
            residual = self.shortcut(x)

        out += residual
        out = self.relu(out)

        return out
class ResNet50_layer4(nn.Module):
    def __init__(self, num_classes= 21 ):
        super(ResNet50_layer4, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 64, 7, 2, 3),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(3, 2, 1)
        )
        self.layer2 = nn.Sequential(
            ResidualBlock(64, 64, 256, False),
            ResidualBlock(256, 64, 256, False),
            ResidualBlock(256, 64, 256, True)
        )
        self.layer3 = nn.Sequential(
            ResidualBlock(256, 128, 512, False),
            ResidualBlock(512, 128, 512, False),
            ResidualBlock(512, 128, 512, False),
            ResidualBlock(512, 128, 512, True)
        )
        self.layer4 = nn.Sequential(
            ResidualBlock(512, 256, 1024, False),
            ResidualBlock(1024, 256, 1024, False),
            ResidualBlock(1024, 256, 1024, False),
            ResidualBlock(1024, 256, 1024, False),
            ResidualBlock(1024, 256, 1024, False),
            ResidualBlock(1024, 256, 1024, True)
        )
        self.layer5 = nn.Sequential(
            ResidualBlock(1024, 512, 2048, False),
            ResidualBlock(2048, 512, 2048, False),
            ResidualBlock(2048, 512, 2048, False)
        )
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(2048, num_classes)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = self.layer5(out)
        out = self.avgpool(out)
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        return out
if __name__ == '__main__':
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = ResNet50_layer4()

    # Create a single input tensor with shape (1, 3, 224, 224)
    input_tensor = torch.randn((1, 3, 224, 224))
