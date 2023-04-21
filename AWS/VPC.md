# VPC

CIDR은 두가지 구성요소가 있다

> Base IP
> 

> Subnet Mask

![image](https://user-images.githubusercontent.com/77326600/233700691-b08af078-e0db-4629-9f23-1ce7b4f6fe4c.png)



/X 일때 

2의 32-X 제곱 만큼의 IP를 갖는다.

/32 일때는 어떤 옥텟도 바뀌지 않고

/24 일때는 마지막 옥텟만 변하고

/16 일때는 뒤에서 2개의 옥텟이 변하고

/8일때는 뒤에서 3개의 옥텟이 변하고

/0 은 모든 옥텟이 변할 수 있다.   

> VPC
> 

새로운 AWS 계정은 모두 기본 VPC가 존재한다.

VPC는 internet connectivity 가 존재하고 EC2 인스턴스는 IPv4 주소를 얻는다.

![image](https://user-images.githubusercontent.com/77326600/230721945-db1998f4-3183-4694-bc03-9b3216252258.png)

라우팅테이블을 확인해보면, 인터넷게이트웨이가 있고 내 계정의 VPC가 존재한다.

VPC 생성!

![image](https://user-images.githubusercontent.com/77326600/230721961-f3d4026a-4591-4d1c-838d-033620ba6547.png)


IPv4 CIDR :10.0.0.0/16
10.0.0.0/16의 IP 주소 범위는 10.0.0.0부터 10.255.255.255까지이며, 이는 총 16,777,216개의 IP 주소를 가집니다.

![image](https://user-images.githubusercontent.com/77326600/230722046-eb7b5e3a-3a2d-462d-bdf7-6ce111a98412.png)

생성한 VPC 안에 서브넷을 생성합니다.

서로 다른 가용영역에 서브넷들을 생성


퍼블릭 서브넷 두 개 생성

![image](https://user-images.githubusercontent.com/77326600/233700959-896271f6-c017-4a56-963f-57e43a949846.png)

서브넷 주소를 다음과 같이 10.0.0.0/24 그리고 10.0.1.0/24로 설정하는 이유는 변경 가능한 옥텟 범위를 고려했기 때문이다.


프라이빗 서브넷 두 개 생성

![image](https://user-images.githubusercontent.com/77326600/233700994-bc29991e-cf42-4942-b45e-a9ae0e3c9a66.png)

두개를 생성할때 publicSubnet 보다 더 넓은 범위를 갖도록 네트워크 주소의 비트를 설정한다.

10.0.16.0/20 은 10.0.16.0~10.0.31.255 까지이다!
