# VPC

CIDR은 두가지 구성요소가 있다

> Base IP
> 

> Subnet Mask
> 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/298d2cad-d223-4b0a-b982-552b5c54ff22/Untitled.png)

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

![image](https://user-images.githubusercontent.com/77326600/230722046-eb7b5e3a-3a2d-462d-bdf7-6ce111a98412.png)

생성한 VPC 안에 서브넷을 생성합니다.

서로 다른 가용영역에 서브넷들을 생성


퍼블릭 서브넷 두 개 생성

![image](https://user-images.githubusercontent.com/77326600/230722077-492a9fc4-3258-4057-9fa3-30f19dcd2d1a.png)


프라이빗 서브넷 두 개 생성

![image](https://user-images.githubusercontent.com/77326600/230722092-02f12619-4f80-473e-88a3-3258d5209c42.png)
