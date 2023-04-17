# Architecture 

![image](https://user-images.githubusercontent.com/77326600/232410956-0d82c7a6-15a2-4749-aab5-ba0049b4a9fe.png)


핵심 포인트는 ALB 입니다.
ALB를 통해서 On-Premise 서버, AWS EC2 에 접근할 수 있습니다.
데이터를 이관하는 동안 On-Premise 서버를 통해 서비스를 유지하며 AWS EC2에 이관하는 방식의 구조입다.
또는 하이브리드 클라우드 방식을 택하여 기존 On-Premise 서버를 유지하며 클라우드 서비스를 이용하는 방식으로 운영하는 것도 하나의 방법이 될 것입니다.

![image](https://user-images.githubusercontent.com/77326600/230462244-99ca6d11-e211-4380-948d-5d9fe2ae4ed5.png)
위처럼 URL을 통해서 대상 그룹에 접근할 수 있는데, 대규모 프로모션 기간에는 행사 상품의 URL을 따로 설정하여 대상 그룹을 만드는 방식도 고려할 수 있을 것 같습니다.
(그렇게 되면 결제 단계에서 결국 합쳐지게 될텐데, 이때는 회원 ID를 쿼리로 하여 또 대상 그룹을 유연하게 묶을 수 있을 것 같습니다.)


## 2. CloudFront - S3 Bucket 연결 및 IAM User 
![image](https://user-images.githubusercontent.com/77326600/230583790-8cb18850-d9dd-4a03-ae27-770e76d9c3a5.png)

CloudFron는 전세계 엣지 로케이션을 활용합니다. S3 Bucket과 연결되어 있으며 이 버킷은 CloudFront만 접근 가능합니다.
캐싱을 통해서 정적 컨텐츠의 빠른 제공을 가능하게 합니다. 

# Funtion Study & Test

### ALB Test

![image](https://user-images.githubusercontent.com/77326600/230463246-bdf88fd4-1843-4cc3-a690-e36cd08f1e18.png)
![image](https://user-images.githubusercontent.com/77326600/230463277-27cea158-55e0-428b-8ea0-0de3eb49f8e5.png)
두 개의 인스턴스를 생성하였습니다.

![image](https://user-images.githubusercontent.com/77326600/230463570-294d861b-4c65-435a-aaad-e0415a4617fa.png)
![image](https://user-images.githubusercontent.com/77326600/230463681-c53978f0-0c67-4e6d-83c5-eba640d5d61e.png)

로드밸런서 생성 과정에서 직접 보안 그룹을 생성하였습니다. EC2 인스턴스로의 부하가 나눠지는지만을 확인하기 위해서 인바운드 규칙을 anywhere로 설정하였습니다.

![image](https://user-images.githubusercontent.com/77326600/230463948-901d3af0-9821-423e-81c8-81e9941953fb.png)
![image](https://user-images.githubusercontent.com/77326600/230463966-234ffe50-683e-4e77-8110-04c058e89ac1.png)

대상 그룹을 생성하고 로드밸런서의 생성까지 완료하였습니다.

![image](https://user-images.githubusercontent.com/77326600/230464143-812677e4-84a4-4948-9316-3105b5a76971.png)
![image](https://user-images.githubusercontent.com/77326600/230464164-b76c49f0-3303-478d-9668-6921f7522de6.png)

동일한 Domain으로 다른 출력 내용을 확인할 수 있습니다.

이것으로 두개의 인스턴스가 동일한 Domain에 매핑된 것을 확인할 수 있습니다.

인스턴스 중 에러가 나서 down된 것이 생기면 그 인스턴스를 제외하고 다른 인스턴스들에 접근을 합니다.

에러에 유연하게 대응할 수 있는 장점을 확인할 수 있습니다.


### CloudFront - S3 Bucket

# Cloud Front

CloudFront = CDN (Content Delivery Network) 

웹사이트의 컨텐츠를 서로 다른 엣지 로케이션에 미리 **********캐싱********** 하여 읽기 성능을 높임

전세계 216개 엣지 로케이션 ( AWS가 지속 추가중)

컨텐츠가 분산되어 있기 때문에 DDoS 예방 가능

(DDoS - 모든 서버가 동시에 공격 받음)

엣지 로케이션의 캐싱 방식으로 !

( 초기 요청은 원본에서 가져오지만, 재요청시에는 캐싱해놓은 것으로 응답함)

**원본 - S3 버킷**

**버킷에는 클라우드프론트만 접근!  !**

**CDN- 전세계 엣지 로케이션 사용.**

**전세계를 대상으로 한 정적 컨텐츠 제공!!**

**캐싱 TTL이 존재함 (대부분 하루)**

교체 리전 복제  

복제를 원하는 각 리전에 이 설정이 되어 있어야 함.

파일은 실시간으로 갱신됨. 캐싱 안되고, 읽기 전용

동적 컨텐츠를 낮은 지연 시간으로 제공하고자 할 때

# CloudFront - S3

S3 버킷 만들기
![image](https://user-images.githubusercontent.com/77326600/230584340-41f1de14-a7e4-4529-9594-132a7c06fea5.png)


![image](https://user-images.githubusercontent.com/77326600/230584384-317002eb-4240-4a41-a518-798c4c8c842e.png)


버킷을 만들고 이미지와 html 파일을 업로드 합니다.

html 파일을 url로 열었을 때 !

![image](https://user-images.githubusercontent.com/77326600/232411099-852a0672-35d2-434b-9d60-922d524d5b42.png)

아직 퍼블릭 설정이 되어있지 않기 때문에 접근이 안됨

![image](https://user-images.githubusercontent.com/77326600/232411165-f7268c1e-be5a-4010-b8f7-254e5a73a9f8.png)

open으로 열었을 때, 이미지가 퍼블릭 되어있지 않아서 이미지가 안보임

CloudFront를 사용하면 파일을 퍼블릭 설정하지 않고도 접근할 수 있음

- CloudFront 만들고 버킷에 access 하기

![image](https://user-images.githubusercontent.com/77326600/232411230-62954c33-e553-4d18-b705-e15e27976466.png)

![image](https://user-images.githubusercontent.com/77326600/232411263-d1eda371-f93a-49b2-b8ee-04c402fd1060.png)

CloudFront에 접근할 때 기본값으로 버킷 안에 있는 index.html을 띄워줍니다.

CloudFront를 생성하고, 버킷 정책을 복사해서 버킷 설정에 그 정책을 붙여넣으면 CloudFront이 성공적으로 배포중이라는 것을 알려주고 그 Domain으로 이동하면

![image](https://user-images.githubusercontent.com/77326600/232411345-7acd3303-5ca0-4fb7-bf7c-c1aa614dac73.png)

이제는 이미지가 보여짐을 알 수 있다!

최초 접근 뒤, 동일 도메인으로 접근하면 CloudFront에서 캐시로 응답한다!

### CloudFront의 원본 엑세스를 확인해보자!

![image](https://user-images.githubusercontent.com/77326600/232411453-fae6d70b-5b35-4899-9e57-304dc69d4c6d.png)
버킷을 원본으로 엑세스함을 알 수 있고, 배포되고 있음을 확인할 수 있다!

![image](https://user-images.githubusercontent.com/77326600/232411487-835b646e-5017-4480-bb36-439ed184da4c.png)
배포 ID = CloudFront ID



