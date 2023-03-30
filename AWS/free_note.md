# AWS

## AWS 클라우드

기업의 IT를 이전하거나 백업과 스토리지, 데이터 분석을 위해서 클라우드를 선택한다

리전 - 데이터 센터의 집합

IAM - 그룹에는 오직 사용자만 배치될 수 있다.

IAM 은 리전 선택을 필요로 하지 않는 글로벌 서비스이다.

사용자와 그룹이 글로벌 관점에서 생성된다.

루트 계정은 모든 권한이 있기 때문에 보안상의 이유로 새로운 관리자 계정을 만들어서 그 계정으로 학습을 진행할 것이다

사용자에 태그를 넣을 수 있다.

그룹에는 정책을 선택할 수 있고, 그 그룹에 속한 사용자는 그 정책을 상속받는다.

사용자가 그룹에 속해있든, 아니든 인라인 정책을 부여할 수 있다.

하나의 사용자가 여러 그룹 안에 들어갈 수 있다.

IMA MFA

- 관리자는 구성을 변경하거나 리소스를 삭제하는 작업을 할 수 있다
- 루트사용자, IMA 사용자를 보호해야 한다
- 비밀번호 +  MFA 토큰 을 사용해서 로그인을 허용하는 방법
    - Vitrual MFA Device

AWS에 엑세스 하는 방법

- AWS Management Console
- AWS Command Line Interface (CLI)
    - 명령줄 인터페이스
- AWS Softwate Developer Kit (SDK)
    
    

### IAM Role

AWS 서비스 몇가지는 우리의 계정에서 실행해야한다. 이를 위해선 어떤 권한이 필요한데, 그러기 위해서는 IAM Role을 만들어야한다

이것은 AWS 서비스에 의해 사용되도록 만들어졌다. 예를들어 EC2 인스턴스를 만든다면, AWS 에서 어떤 작업을 수행하려 할텐데 그러기 위해선 IAM Role을 만들어 결합하여 하나의 객체로 만들어야 한다. EC2 인스턴스가 AWS의 어떤 정보에 접근하려고 할 때 IAM Role을 확인할 것이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5202fb07-880a-4323-a16b-53434ddd5d15/Untitled.png)

IAM 사용자 그룹은 다른 사용자 그룹을 포함할수 없고, IAM 사용자만을 포함할 수 있다

IAM 정책의 문장은 효과,원칙,조치,리소스,조건 으로 구성된다. 버전은 IAM 정책의 일부이지 문장의 일부가 아니다.

그룸은 오직 사용자만 가질수 있다.

**예산 설정**

루트 계정에서 IAM 계정도 예산 설정에 대한 권한을 갖도록 위임하고,

IAM 계정으로 예산 설정을 하였다.

Budgets 메뉴에서 설정할 수 있고, 예상 예산, 실제 예산에 대한 임계치 비율을 설정하여 이에 도달하면 메일로 알림을 받게 할 수도 있다.

### EC2 인스턴스

Elastic Computer Cloud 로서 OS, CPU,RAM,Sotrage,Network Card, Firewall, Bootstrap script 로 이루어진 가상환경이다.

Bootstrap script의 script는 EC2 생성시 딱 한번 쓰이는데 EC2의 설정을 script로 구성해주는 역할이다.-

EC2 Instance Types

m5.2xlarge 

m : instance class

5: generation

2xlarge : size within instance class

EC2 인스턴스는 보안그룹이 감싸고 있다. 보안그룹은 EC2에 접근하는 inbound traffic, EC2에서 외부로 접근하는 Outbound traffic에 대한 권한 및 규제를 담당하는데 보통 IP 범위는 IPv4 또는 IPv6를 허용하고, 밖으로 접근하는 outbound traffic에 대해서는 항상 열려있다.

보안 그룹은 다른 보안그룹과 묶여서 쓰일 수 있는데, 여러개의 보안그룹과 붙여서 쓰일 수 있다.

region , VPC 에 결합하여 설정되므로 이것들이 바뀔경우 보안그룹도 재설정이 필요하다.

SSH 접근을 위한 보안그룹을 따로 두는것이 좋다고 한다.

기본적으로 inbound traffic = blocked, outbound traffic = authorized 상태이다.

보안그룹으로 IP는 신경쓰지 않고 보안그룹들의 정책만을 신경써서 접근을 제어할 수 있다

************************Classic Port************************

- 22 = SSH (Secure Shell)
- 21 = FTP
- 22 =SFTP (Secure file Transfer)
- 80 = HTTP
- 443 = HTTPS
- 3389 = RDP (Remote Desktop Protocol) - Log into a window instance

EC2 인스턴스에 접근하기!

EC2 인스턴스를 보안그룹을 알맞게 설정하여 생성한다

ssh all

http all

그리고 key pair 파일(.pem)을 받은 후 

ssh -i (key pair 파일 위치 \ 파일이름.pem) ec2-user@(인스턴스 public ip) 로

powershell에서 위 명령어를 실행해주면

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a71d8fd-8841-4741-9670-ef423fc3629a/Untitled.png)

이렇게 성공적으로 인스턴스에 접근할 수 있게 된다.

**EC2 인스턴스 결제 옵션**

- on Demand
    - 쓴 만큼만 내는 방식
    - 비용이 초당 청구됨.
    - 선결제가 필요 없지만 높은 가격
    - short-term, un-interrupted workloads에 추천
- Reserved Instance
    - 예약 방식
    - 높은 할인율 75% 정도
    - 1년 또는 3년중에서만 고를 수 있음 (3년이 더 높은 할인율)
    - 모두 선결제 하면 더 싸짐
        - 매 월 결제, 부분 선결제, 전체 선결제가 있음
    - 데이터베이스에 적합함
    - 전환 가능 예약 인스턴스가 있는데 이것은 비교적 낮은 할인율을 갖고있음
- Savings Plans
    - 장기 사용에 할인을 줌
    - 정해진 기간, 정해진 시간동안에 해당하는 돈을 지불함
    - 정해진 시간에만 쓰고 이 시간을 장기적으로 사용할 때 씀
- Spot Instance
    - 높은 할인율
    - 언제든 중단 가능
    - DB에는 절대 쓸 수 없음
    - 보다 더 높은 가격을 제시한 사람이 나오면 뺏길 위험이 있음
    - 스팟 가격은 점진적으로 변하는데 최고가를 지불할 의향이 있을때만 쓸 수 있음
    - 언제 끊겨도 괜찮은 작업에 쓰임
- Deditacte Hosts
    - AWS 센터 내 하나의 서버 전체 임대
    - 규정을 준수해야함
    - 가장 비싼 옵션
    - 하드웨어에 접근할 수 있고, 다른 사용자와 공유하지 않기에 안전성이 있음
- Dedicated Instance
    - Dedicated Host의 약한 버전
    - 하드웨어에 접근 불가능
- Capacity Reservations
    - 사용하지 않을때도 결제한 방식
    - 필요할때마다 사용 가능
    - No time commitment
    - On-demand와 반대 개념

### 스팟인스턴스

항상 Spot instance의 최고가를 지불해야함

spot instance가 끊길경우 정지했다가 다음에 다시 spot instance를 잡게되면 그때 다시 실행할지, 아니면 아예 instance를 terminate할지를 선택해야함

- spot block : 특정 시간동안 스팟 인스턴스를 막아둠. 보통 인스턴스를 뺏기지 않게 됨

요청의 종류에는 one-time 요청, persistent 요청이 있는데 one time 요청을 하게 되면 스팟 요청이 일회성이기 때문에 인스턴스를 뺏기게 될 수 있음

지속적 요청을 하게되면 인스턴스가 종료되더라도 계속해서 요청을 하게되므로, 인스턴스가 유지됨

따라서 persistene 요청하면 인스턴스를 종료할 때 spot 요청 취소 → instance 종료 순으로 가야함

spot instacne는 인스턴스 유형과 가용 영역을 사용자가 지정하는 방식이고,

spot fleets는 사용자의 요구 조건에 따라 최적의 선택으로 알아서 정해줌

퀴즈 오답

- 일련의 EC2 인스턴스에 호스팅 될 애플리케이션을 실행하려 합니다. 이 애플리케이션에는 소프트웨어 설치가 필요하며, 최초 실행 중에 일부 OS 패키지를 업데이트해야 합니다. EC2 인스턴스를 실행하려는 경우, 이를 위한 최적의 방식은 무엇일까요?
    - 필수 소프트웨어의 설치 및 OS 업데이트를 수행하는 bash 스크립트를 작성한 후, 이 스크립트를 인스턴스 실행시에 EC2 사용자 데이터에서 사용하기
    - EC2 사용자 데이터는 bash 스크립트를 사용해 EC2 인스턴스를 부트스트랩 할 경우에 사용됩니다. 이 스크립트에는 소프트웨어/패키지 설치, 인터넷에서 파일 다운로드 등, 여러분이 원하는 작업을 수행하기 위한 명령어를 포함시킬 수 있습니다.
    - 
- 온프레미스에 호스팅된 OLTP 데이터베이스를 갖춘 전자 상거래 애플리케이션이 있습니다. 이 애플리케이션은 인기가 좋아, 데이터베이스가 초당 수천 개의 요청을 지니게 됩니다. 여러분은 데이터베이스를 EC2 인스턴스로 이전하려 합니다. 이렇게 높은 빈도를 보이는 OLTP 데이터베이스를 처리하기 위해서는 어떤 EC2 인스턴스 유형을 선택해야 할까요?
    - 스토리지 최적화
    - 스토리지 최적화 EC2 인스턴스는 로컬 스토리지의 대규모 데이터 세트에 대해 높은 수준의, 그리고 순차적인 읽기/쓰기 액세스 권한이 필요한 워크로드에 적합합니다.

ssh로 EC2 인스턴스에 접근하면

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75c479ad-f01d-4237-9348-d5e66ac71253/Untitled.png)

사용자의 사설 ip를 알 수 있다

공용 IP에 접근하고 나서야 사설 IP에 접근을 할 수가 있다.

공용ip : IPv4

사설ip : IPv6

공용 IP는  world wide 범위에서 고유한 값을 갖고있지만, 사설 IP는 공용 IP 내부에서만 고유한 값을 갖고 있으면 된다. 한 네트워크 안의 사설 IP는 서로 통신할 수 있고, NAT나 GateWay를 거쳐야만 다른 네트워크와 통신할 수 있다

인스턴스를 껐다가 키면 public ip가 바뀌는것을 확인할 수 있다.

공용 ip가 바뀌지 않도록 하기 위해서는 elastic ip를 사용해야 한다

elastic ip를 빌려서 인스턴스에 연결할 수 있다.

### 배치그룹 (Placement Group)

- Cluster
    - Single Available zone, Low Latency
    - 매우 빠르지만 하나의 AWS랙을 공유하기 때문에 에러에 취약함
- Spread
    - 가용 범위 안에서 EC2를 최대 7개 둘 수 있음
    - 한 가용 범위에서 EC2가 에러떠도, 다른 EC2가 버틴다면 문제 없음
- Partition
    - 각각 AWS 랙을 사용함
    - 서로 다른 HardWare
    

### 퀴즈

- 스팟 플릿은 한 세트의 스팟 인스턴스로 선택적 온디맨드 인스턴스이다
- EC2 절전 모드를 활성화하기 위해서는 인스턴스 루트 볼륨 유형이 EBS 볼륨이어야만 하며, 민감한 내용을 보호할 수 있도록 암호화되어야 합니다.

### EBS volume

Network drive can attatch to instances while they run

네트워크 USB 스틱 이라고 생각하면 편하다.

(같은 가용 범위 안에서만 사용 가능하다)

하나의 인스턴스에 두개의 EBS Volume이 연결되는것은 가능하다

(하나의 머신에 두개의 USB 스틱이 꽂히는게 가능하듯)

하지만 하나의 EBS Volume이 여러개의 인스턴스에 꽂히는건 불가능하다

(USB 스틱은 한 머신에만 꽂힐수 있듯)

또한 EBS Volume은 인스턴스에 연결이 되지 않은 상태로 있을 수 있다

인스턴스가 종료될 때 Root EBS가 기본적으로 삭제되게 설정되지만 이는 변경할 수 있고, 인스턴스가 종료될 때 다른 EBS 들은 삭제되지 않으며 이는 변경 불가능하다

EBS의 정보를 다른 가용영역으로 옮길 수 있는 방법이 있다.

EBS snapshot을 찍고, 그 스냅샷을 다른 가용역역에서 복구할 수가 있다.

EBS 스냅샷 아카이브 : 스냅샷보다 싼 가격이지만 복구하는데 시간이 오래 걸린다

스냅샷 휴지통 : 실수로 삭제했더라도 보관되며, 보관 기간이 1일부터 1년까지 이다

Fast Snapshot Restore : 스냅샷의 초기화를 강제화하여 초기 사용에 지연이 없게한다.  (비싼 가격)

### AMI

Amazone Machine Image

EC2 인스턴스를 customizaion 한 것이다

특정 region 에서만 사용된다 → region의 경계를 넘어서 복사될 수 있다

********************ami 종류********************

- public ami
- own ami
- marketplace ami

******************************AMI 프로세스******************************

1. 인스턴스를 만들고 cutomize 한다
2. 인스턴스를 중지한다
3. ami를 빌드한다
4. 다른 인스턴스에서 ami를 통해서 launch 한다

EC2 인스턴스 스토어를 통해서 하드웨어 성능을 업그레이드 할 수 있다.

EC2 인스턴스 스토어는 최적의 디스크 I/O 성능을 제공합니다.

**************EBS Volume types**************

GP2/GP3 (SSD) : 가장 일반적임. 가성비가 좋음

IO2/IO3 (SSD) : 높은 성능의 SSD, low-latency , high-throughput workloads + 여러 인스턴스에 연결 가능 (최대 16개 까지)

EBS 다중 연결을 사용하면, 동일한 EBS 볼륨을 동일 AZ 상에 있는 다수의 EC2 인스턴스에 연결할 수 있습니다. 각 EC2 인스턴스는 완전한 읽기/쓰기 권한을 갖게 됩니다

EC2 인스턴스를 생성할 때, 부팅 볼륨으로는 다음의 EBS 볼륨 유형만을 사용할 수 있습니다: gp2, gp3, io1, io2, Magnetic(표준)

************************************************EFS Elastic File System************************************************

리눅스 에서만 사용 가능

사용한 만큼만 비용을 냄

- scale
- performance mode
- throughput mode
    - regarldess of storage size ( provision)

**EFS Storage class**

- Standard
- EFS - IA
    - 검색 비용이 있지만 저장 비용은 낮음
    - 수명 주기 정책에 따라서 standard 에서 EFS- IA로 계층이 이동됨

가용성과 주기성

standard : 멀티 가용범위

one-zone : 하나의 가용범위

### EBS vs EFS

******EBS******

- 하나의 인스턴스에만 결합
- 가용범위 존재
- gp2 - 디스크 사이즈가 커지면 IO 증가함
- IO1 - IO에 상관없이 증가 가능
- 다른 AZ로 이주하려면 스냅샷을 찍고 그 스냅샷을 다른 AZ에서 복구하는 방법으로 이전함
- 애플리케이션이 실행하지 않을 때만 백업 가능
- 루트 EBS 볼륨은 인스턴스가 종료되면 같이 종료됨 (설정 변경 가능)

******EFS******

- 수백개의 인스턴스에 결합 가능
- AZ의 경계를 넘나들 수 있음
- 리눅스에서만 사용 가능
- EBS보다 비쌈
- EFS-IA로 비용을 절약할 수 있음
- 사용한 만큼만 지불함

  

퀴즈

- **EBS 다중 연결이란 무엇일까요?**
• **동일한 EBS 볼륨을 동일한 AZ에 있는 다수의 EC2 인스턴스에 연결**
- **기반 스토리지에 310,000의 IOPS가 필요한 고성능 데이터베이스를 실행하고 있습니다. 어떤 방법을 추천할 수 있을까요?**
• **EC2 인스턴스 스토어 사용**
(EC2 인스턴스에서 데이터베이스를 인스턴스 스토어를 사용하여 실행 가능하지만, EC2 인스턴스가 중지 시 데이터가 손실이라는 문제가 있습니다 (문제 없이 다시 시작할 수 있음). 한 가지 솔루션은 인스턴스 스토어가 있는 다른 EC2 인스턴스에서 복제 메커니즘을 설정하여 대기 복사본을 가질 수 있다는 것입니다. 또 다른 솔루션은 데이터에 대한 백업 메커니즘을 설정하는 것입니다. 요구 사항을 검증하기 위해 아키텍처를 설정하는 방법은 모두 사용자에게 달려 있습니다. 이 사용 사례에서는 IOPS 기준이므로 EC2 인스턴스 스토어를 선택해야 합니다.)

### 확장성 & 가용성

확장성 scalability 는 어플,시스템이 더 많은 부하를 견딜수 있도록 컨트롤이 가능한 성질이다.

확장성에는 두 종류가 존재하는데 Vertical Scalability (수직 확장성) , Horizontal Scalability (수평 확장성) 이 그 종류이다.

수직 확장성은 인스턴스 한개 자체의 사이즈를 키우는 것이다.

수평 확장성은 인스턴스의 개수 자체를 늘리는 것이다. (스케일 인, 스케일 아웃 이다)

수직 확장성은 DB와 같이 분배되지 않은 시스템에 사용하기 용이하고, 수평 확장성은 웹이나 현대 어플리케이션처럼 분배된 시스템에 용이하다. AWS의 기술로 인해 최근에 수평 확장에 더 쉽게 접근할 수 있다.

높은 가용성은 여러 곳에 센터를 두는것을 떠올리면 된다.

한 AZ에서 문제가 발생하더라도 버텨주는 다른 AZ가 존재하기 때문에 에러이슈가 발생해도 견딜수 있다.

### 로드밸런서

부하를 분산해주는 기능을 제공함

인스턴스의 상태를 체크해주고, 인스턴스와 보안그룹으로 결합하여 보안성을 강화함.

인스턴스는 로드밸런서에서 직접 오는 연결만 받아야 되기에 보안그룹으로 묶여있음.

user - LOAD BALANCER - EC2

**ALB (Application Load Balancer)** 

EC2를 대상 그룹으로 묶어서 관리함

URL에 따른 매핑을 해주기도 하고, 하나의 로드밸런서가 여러개의 대상그룹을 관리할 수 있음

호스트네임은 고정되어있지만, 서버는 클라이언트의 IP를 직접적으로 알 수 없고, X-Forwarded-For 이라는 헤더에 실제 클라의 IP가 삽입되어 있음

********NLB(Network Load Balancer)********

Layer 4 

TCP ,UDP 트래픽 관리

ALB보다 빠른 속도

AZ에 고정 IP를 갖고있고, 탄력적 IP 역시 지원 가능함

극강의 성능, TCP, UDP가 나오면 NLB를 떠올리자

(프리티어는 아님)

ALB와 같이 대상그룹으로 묶어서 관리를 하지만 HTTP에 더해 TCP 처리가 가능함

사설 IP를 이용함.

### GWLB

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eee9c431-6343-4bff-ba24-c4174e993f3b/Untitled.png)

GateWay Load Balancer

트래픽을 분석해주는 역할을 수행함

네트워크 싱글 게이트웨이 역할을 수행함

가장 낮은 계층 Layer 3에서 작동함

6081 포트를 기억하자!

ELB

ELB 고정 세션 기능은 동일한 클라이언트에 대한 트래픽이 항상 동일한 대상으로 리다이렉트되도록 해줍니다(예: EC2 인스턴스) 이는 클라이언트들이 세션 데이터를 소실하지 않게 해줍니다.

다음의 쿠키 이름은 ELB가 선점하고 있습니다(AWSALB, AWSALBAPP, AWSALBTG).

퀴즈 오답

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/db1049e8-9747-4839-a0e0-4850ca30590e/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/acedc1bb-8e9e-4f2c-9082-af8144e4720f/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/50753cad-f085-4ca3-99f1-612b794b64fb/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3043ec89-14f8-4a09-8097-c57f5f116687/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bfa6ac1e-2567-4cda-8089-b67ade5f93c9/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7b5c61fa-6639-43f1-965a-2a1e8573e099/Untitled.png)

### Amazone RDS

AWS에서 관리하는 클라우드안에 다음과같은 DB를 생성할 수 있다

- Postgres
- MySQL
- MariaDB
- Oracle
- Ms SQL Server
- Aurora

RDS는 관리 서비스이다.

자동 감독, OS 패치, 특정 시간대로 백업-복구 가능(Timestamp), 모니터링 대시보드,읽기 복제 ,EBS를 통한 백업 가능

SSH는 사용할 수 없다.

**Storage Auto Scaling 기능**

남은 용량이 10%미만일때 + 저장 공간 부족이 5분 이상 지속될 때 + 최근 수정이 6시간 전일 때 자동으로 저장공간이 수정된다.

알아서 자동으로 스케일링 해주기 때문에 예측불가능한 workloads에 유용하게 쓰인다!

읽기 전용 DB는 비동기 복제되어 만들어지고 , 읽기 DB는 select만 가능하다! (Insert,Update,Delete 불가)

읽기 전용 DB는 cross region하게 복제될 경우 비용이 발생한다.

읽기 전용 DB는 재난 상황을 대비하여 Multi Region하게 구축 가능하다.

DB를 늘리는데에 있어서 지연시간이 존재하지 않으며, shapshot을 통해서 만들어진다.

RDS Custom은 관리자 권한을 갖는 DB이며 Oracle과 MS SQL 에서 사용 가능하다

******Amazone Aurora******

- Postgres , MySQL에 사용 가능하다
- 15개의 복제본을 가질수 있다
- 높은 가용성과 Read Scaling
    - 3 AZ에 6개의 카피가 생성된다
    - 쓰기를 위해선 6개중 4개가 필요하고
    - 읽기를 위해선 6개중 3개가 필요하다
    - 하나의 마스터 인스턴스가 존재한다
    - self healing이 되며 빠른 장애 조치가 가능하다
- 오토 스케일링을 지원한다
- 커스텀 엔드포인트를 설정할 수 있으며, 커스텀 엔드포인트에 연결되지 않은 인스턴스는 사라지지는 않지만 사용되지는 않는다
- 멀티 마스터를 사용할 수 있다
    - write node의 가용성이 올라간다
- 장애 발생시 읽기전용 인스턴스가 마스터 인스턴스로 승격한다

**********************************자동 백업 vs 수동 DB 스냅샷**********************************

자동 백업

- 전체 DB 백업
- 시간이 지나면 사라짐 (1일~35일)
- 5분마다 백업

수동 DB 스냅샷

- 수동으로 범위 설정
- 원하는 기간만큼 보유 가능
- 자동 백업보다 훨씬 저렴함

********************RDS 복구******************** 

- 온프레미스 DB 백업
- S3에 저장
- 새 RDS 인스턴스에 백업

****AURORA 복구****

- Percona XtraBackup을 사용하여 온프레미스 DB 백업
- S3에 저장
- 새 Aurora Cluster에 백업

****************************AURORA 복제****************************

- 스냅샷보다 빠름
- 같은 클러스터 볼륨 사용

****************RDS & AURORA 암호화****************

- AWS KMS 사용
- 마스터가 암호화 되지 않으면 읽기 복제본도 암호화 되지 않음
- SSh 사용 불가

****RDS 프록시****

- DB 커넥션 풀을 만들어 프록시로 감당함
- DB에 부하를 줄이고 빠른 장애 조치 가능함
- IAM 인증을 강제화함

************************Elastic Cache************************

- DB 부하 줄임
- 캐시 히트, 캐시 미스 있음
- 캐시 미스시 DB에서 캐시로 데이터 저장해놓음
- stateless 하게!
- Redis
    - 멀티 AZ
    - 읽기 복제본
    - 백업 가능
    - 실시간 순위 업데이트 기능
- MemCached
    - 멀티 파티셔닝 (샤딩)
    - 가용성 x
    - 지속성 x
    - 단순 분산 캐시
- 캐시 보안
    - IAM 인증 사용 안함
    - 캐시 생성,삭제시에만 IAM 정책 사용
    - 레디스에서는 패스워드,토큰을 사용함
    - 레디스에서 SSL 가능
    - Memcached에서는 SASL 가능

**퀴즈 오답**

![https://blogfiles.pstatic.net/MjAyMzAxMTlfOSAg/MDAxNjc0MDU5NDI1OTc5.3ElJNn4lu1w1UJPmjSgjNp-ruFf5-G4XM7EAsLTZPhwg.TxyLYK4DHHm1NFQHmVfvHY-wMhDdWuTH_lEGCVOoRKAg.PNG.georgeking98/image.png?type=w1](https://blogfiles.pstatic.net/MjAyMzAxMTlfOSAg/MDAxNjc0MDU5NDI1OTc5.3ElJNn4lu1w1UJPmjSgjNp-ruFf5-G4XM7EAsLTZPhwg.TxyLYK4DHHm1NFQHmVfvHY-wMhDdWuTH_lEGCVOoRKAg.PNG.georgeking98/image.png?type=w1)

![https://blogfiles.pstatic.net/MjAyMzAxMTlfMjQ0/MDAxNjc0MDU5NDkyODI2.MOFPeR-hKShYjBK-j3A-b9xmj1--uY2vHuoPs4JfeAwg.AGJIhl-lUvGl-cmyi0IuSGhwf60ZDrtzRFOUM5-ehJUg.PNG.georgeking98/image.png?type=w1](https://blogfiles.pstatic.net/MjAyMzAxMTlfMjQ0/MDAxNjc0MDU5NDkyODI2.MOFPeR-hKShYjBK-j3A-b9xmj1--uY2vHuoPs4JfeAwg.AGJIhl-lUvGl-cmyi0IuSGhwf60ZDrtzRFOUM5-ehJUg.PNG.georgeking98/image.png?type=w1)

**읽기 전용 복제본은 DNS 이름을 갖는 새로운 엔드 포인트를 추가한다.**

**다중 AZ는 활성화 상태의 데이터베이스 종류와 상관 없이 동일한 연결 문자열을 유지합니다.**

![https://blogfiles.pstatic.net/MjAyMzAxMTlfMjMw/MDAxNjc0MDU5NjQ3ODA5.2lZBDr5Fy1cMuX4aVlQlz3bGP41_mUXQ6gH6dRfuuEkg.9f5Bb5jehiMuOVWcnmN2oyS2PVxsJU29bslPtA2d6zMg.PNG.georgeking98/image.png?type=w1](https://blogfiles.pstatic.net/MjAyMzAxMTlfMjMw/MDAxNjc0MDU5NjQ3ODA5.2lZBDr5Fy1cMuX4aVlQlz3bGP41_mUXQ6gH6dRfuuEkg.9f5Bb5jehiMuOVWcnmN2oyS2PVxsJU29bslPtA2d6zMg.PNG.georgeking98/image.png?type=w1)

**읽기 전용 복제본은 재해 복구에 도움이 되지 않습니다.**

**Aurora 글로벌 데이터베이스를 사용하면 최대 5개의 2차 리전까지 Aurora 복제본을 가질 수 있습니다.**

![https://blogfiles.pstatic.net/MjAyMzAxMTlfMjkz/MDAxNjc0MDU5ODAyMjk0.dnd6x2d81r-DXrOaX83FFlReYqAvtWykV18-NM2C0Qcg.LTK2T-xq63Yep0-p5DrL6E8Hinq3evrPk5HRIIrQp4Eg.PNG.georgeking98/image.png?type=w1](https://blogfiles.pstatic.net/MjAyMzAxMTlfMjkz/MDAxNjc0MDU5ODAyMjk0.dnd6x2d81r-DXrOaX83FFlReYqAvtWykV18-NM2C0Qcg.LTK2T-xq63Yep0-p5DrL6E8Hinq3evrPk5HRIIrQp4Eg.PNG.georgeking98/image.png?type=w1)

![https://blogfiles.pstatic.net/MjAyMzAxMTlfMjYw/MDAxNjc0MDU5ODg2ODc0.0u24WuvAvYscpkxF75hIuLz3PUMcAURroP8ePXJKak4g.lpJIpeS4eeW3rEKvoeBS9CJHOv3q01e57kiN3FkSjQog.PNG.georgeking98/image.png?type=w1](https://blogfiles.pstatic.net/MjAyMzAxMTlfMjYw/MDAxNjc0MDU5ODg2ODc0.0u24WuvAvYscpkxF75hIuLz3PUMcAURroP8ePXJKak4g.lpJIpeS4eeW3rEKvoeBS9CJHOv3q01e57kiN3FkSjQog.PNG.georgeking98/image.png?type=w1)

**암호화 되지 않은것을 암호화 하기 위해선 스냅샷이 필요하다**

![https://blogfiles.pstatic.net/MjAyMzAxMTlfMTkw/MDAxNjc0MDU5OTgzOTUy.Pa0S8SWXquVgbar5jj1gWR_EcJa7ZzH3ffhwZUG68pcg.OneHHGRSFP6x0HDiJBysuFwS9tmHs40C_rchB7ncRMkg.PNG.georgeking98/image.png?type=w1](https://blogfiles.pstatic.net/MjAyMzAxMTlfMTkw/MDAxNjc0MDU5OTgzOTUy.Pa0S8SWXquVgbar5jj1gWR_EcJa7ZzH3ffhwZUG68pcg.OneHHGRSFP6x0HDiJBysuFwS9tmHs40C_rchB7ncRMkg.PNG.georgeking98/image.png?type=w1)

**IAM 인증 지원 - Postgres , MySQL**

![https://blogfiles.pstatic.net/MjAyMzAxMTlfMjAz/MDAxNjc0MDYwMDc4MzI3.VJdmnif3rz6Ybk2_vijdgNwqlBECBbbbzLtFeTyJMoUg.ut7RdpdNK4JwLAYYcMJZ7Y1XXyHT9EictfrTmS6HmBcg.PNG.georgeking98/image.png?type=w1](https://blogfiles.pstatic.net/MjAyMzAxMTlfMjAz/MDAxNjc0MDYwMDc4MzI3.VJdmnif3rz6Ybk2_vijdgNwqlBECBbbbzLtFeTyJMoUg.ut7RdpdNK4JwLAYYcMJZ7Y1XXyHT9EictfrTmS6HmBcg.PNG.georgeking98/image.png?type=w1)

**많은 양의 워크로드 수행과 스케일이 축소된 , 대부분 시간동안 사용되지 않을 때는 아우라 서버리스**

**************라우팅************** 

퀴즈
