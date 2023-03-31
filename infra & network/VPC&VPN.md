# VPC , VPN

### **************Amazon Virtual Private Cloud**************

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec8cc26a-1fc0-4925-b27a-006f7b3ca73c/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/870cf4aa-bc17-4abe-b99f-b2eaf835babd/Untitled.png)

VPN ⇒ 가상 사설망

네트워크 A , 네트워크 B가 실제로 같은 네트워크상에 있지만 논리적으로 다른 네트워크인것 처럼 작동

암호화된 터널을 만들어서 데이터를 전송하고 IP 주소를 숨겨 온라인 상에서 정보를 보호해줌

멀리 떨어진 네트워크 환경을 하나의 안전한 네트워크로 만든다.

ex) 회사 내에서만 접속 가능한 서버를 VPN을 이용해서 집에서도 회사 내부 네트워크에 있는 것처럼 만든다

**VPC**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/da9e8a7c-3c40-4aca-b23a-be4b932b5249/Untitled.png)

VPC가 없다면 EC2 인스턴스들이 서로 거미줄처럼 연결되고 인터넷과 연결됨

⇒ 시스템 복잡도 끌어올림

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5bd57e24-694b-4f73-968b-ea0e7d6c975d/Untitled.png)

VPC를 적용하면 위 그림처럼 VPC별로 네트워크를 구성할 수 있음.

각각의 VPC는 완전히 독립된 네트워크처럼 작동하게 됨.
