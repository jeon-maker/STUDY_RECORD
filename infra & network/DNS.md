# DNS

******Domain Name Service******


![image](https://user-images.githubusercontent.com/77326600/229361384-66cc55aa-4ced-4313-957a-1793ebc97a85.png)


1. web browser → Local DNS Server
    - Local DNS Service - 회사에 의해 관리되거나 인터넷 서비스 제공자에 동적으로 할당됨
2. Local DNS Server가 처음 보는 쿼리일 경우
    1. Local DNS Server 가 Root DNS Server에 물어봄 ( ICANN에 의해 관리됨)
        1. Root DNS Server의 대답 : 본 적 없지만 .com은 알고 있어.
        2. .com은 이름 서버 레코드로 공인IP 1.2.3.4로 가봐~
    2. Local DNS Server가 Root DNS Server의 응답을 받고 TLD DNS Server 1.2.3.4에 요청을 보냄
        1. TLD DNS Server는 알 수 없는 쿼리이기 때문에 당장 답할 수가 없음
        2. 하지만 요청에 대한 NS (Name Server는 알고 있음)
            1. NS = 도메인 이름과 IP의 상호변환을 가능하게 해주는 서버
        3. 요청에 해당하는 NS의 IP 5.6.7.8 로 가봐~
    3. Local DNS Server가 TLD DNS Server의 응답을 받고 SLD DNS Server 5.6.7.8에 요청을 보냄
        1. SLD DNS Server에 요청을 보냄 (도메인 이름 레지스트라에 의해 관리됨 ex 아마존 Route 53)
        2. SLD DNS Server에는 쿼리에 해당하는 응답이 가능함.
        3. 레코드 정보와, IP 를 알려줌
    4. 이제 받은 IP를 토대로 웹브라우저에 답변을 하고, 나중에 같은 요청이 올 경우에는 즉각적으로 응답 가능
