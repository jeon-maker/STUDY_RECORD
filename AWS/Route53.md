# Route 53

고가용성, 확장성을 갖춘 DNS

고객이 DNS 레코드를 제어할 수 있음 → DNS에 대한 완전한 제어권을 갖고 있음

Client → Route 53 

- 도메인에 해당하는 쿼리를 보냄

Route 53 →Client 

- 도메인에 해당하는 IP를 알려줌

Client가 요청을 받고 바로 인스턴스에 접근함 !

Route 53은 도메인 이름 레지스트라로, 받은 쿼리를 도메인 이름으로 등록 

### Record Types

- A - maps a hostname to IPv4
- AAAA - maps a hostname to IPv6
- CNAME - maps a hostname to another hostname
    - 대상 호스트 이름 : A / AAAA 레코드
- NS - Name Servers for the Hosted Zone
