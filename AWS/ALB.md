# ALB

### ALB

- 머신 간 다수 HTTP 애플리케이션의 라우팅에 사용
    - 머신들은 대상 그룹으로 묶임
- 동일 EC2 인스턴스 상의 여러 애플리케이션에 부하 분산
- URL에 따라서 대상 그룹에 라우팅 됨

![image](https://user-images.githubusercontent.com/77326600/232413298-c8d0479a-3a6c-4f6c-9c69-77e099b12f59.png)

- ************************대상 그룹************************
    - EC2 인스턴스가 대상 그룹이 될 수 있음

![image](https://user-images.githubusercontent.com/77326600/232413341-f1348707-8549-4b58-9fdf-ba02cf13a514.png)

- ALB는 대상 그룹에 따라서 부하를 분산하는데, 대상 그룹은 URL에 따라 다르게 설정할 수 있다.
    
    위 사진은 AWS EC2가 모바일 부하를 담당하고, On-premises 서버가 Desktop 부하를 담당하는
    
    모습이다
    
- 클라이언트의 IP를 애플리케이션 서버는 알지 못한다. X-Forwarded-For에 삽입된다.

![image](https://user-images.githubusercontent.com/77326600/232413619-d5ef1374-ad13-4db0-a386-5443cbe2d293.png)

- 클라이언트가 ALB에 접속 → Connection termination 기능 → EC2에는 로드밸런서  IP로 접근

⇒ 서버가 클라이언트의 IP를 알 수 없음! ( 알려면 X - Forwarded - For을 알아야 함)

### ALB Test

![image](https://user-images.githubusercontent.com/77326600/232413752-72f2c517-ad60-4be9-aa38-bf907a7615e5.png)

![image](https://user-images.githubusercontent.com/77326600/232413793-b19d8c12-d2d0-4e68-8ff9-7c8368318a56.png)

로드밸런서 생성과정에서 직접 보안그룹을 만들고 있습니다.

![image](https://user-images.githubusercontent.com/77326600/232413866-c5a612eb-80d3-4086-8002-5435c51ce5da.png)


우선 EC2 테스트를 위해 인바운드 규칙을 anywhere로 설정합니다.

![image](https://user-images.githubusercontent.com/77326600/232413950-ff55c09a-5365-4ef0-b4ce-d63ca34495e2.png)

로드밸런서의 보안그룹을 생성하였습니다.

![image](https://user-images.githubusercontent.com/77326600/232414009-863b92ef-9ebe-4513-82ce-30afef7ff94c.png)

로드밸런서를 사용하기 위해서 타겟그룹을 만들어 주었습니다.

![image](https://user-images.githubusercontent.com/77326600/232414074-4978525c-b37b-4d74-b0df-c60443e9e183.png)

대상 그룹을 생성하고 그 안에 인스턴스들을 넣었습니다.

![image](https://user-images.githubusercontent.com/77326600/232414141-ba3d8a07-6faf-4e55-89bb-c356563821c1.png)

로드밸런서의 생성을 완료하였습니다

![image](https://user-images.githubusercontent.com/77326600/232414187-0104bfcf-9fac-41ae-b5d2-826ac06fac82.png)


동일한 Domain으로 다른 출력 내용을 확인할 수 있습니다.

이것으로 두개의 인스턴스가 동일한 Domain에 매핑된 것을 확인할 수 있습니다.

인스턴스 중 에러가 나서 down된 것이 생기면 그 인스턴스를 제외하고 다른 인스턴스들에 접근을 합니다.

에러에 유연하게 대응할 수 있는 장점을 확인할 수 있습니다.

### 보안 강화하기 - 1. 인스턴스의 보안그룹 설정으로 로드밸런서를 통해서만 접근 가능하게 !

로드밸런서에 접근시 로드밸런서의 보안그룹에 접근 → 인스턴스에 접근시 인스턴스의 보안그룹에 접근

![image](https://user-images.githubusercontent.com/77326600/232414263-09d0733b-3ac4-485b-9ff4-87285f786796.png)

EC2 보안그룹의 인바운드 규칙을 모든 트래픽 허용 → 로드밸런서로부터 오는 것만 허용하기!

![image](https://user-images.githubusercontent.com/77326600/232414329-4086ef59-4b18-45ed-bc68-40e32eaff12e.png)

로드밸런서를 통해서만 접근 가능하도록 하기!!

그 결과 인스턴스에 직접 접근 불가! 

### 보안 강화하기 - 2. 로드밸런서에 규칙 적용

![image](https://user-images.githubusercontent.com/77326600/232414370-dda59816-0db7-41b0-b91a-5bc78001f7f0.png)

현재는 로드밸런서에서 무엇이든 대상 그룹으로 보낼 수 있게 되어있습니다.

![image](https://user-images.githubusercontent.com/77326600/232414391-91e04381-a23c-4e90-90d0-63ef329745c3.png)

로드밸런서에서 custom으로 path 규칙을 설정하여 에러 발생시 에러 문구를 띄운 모습입니다.
