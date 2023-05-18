### 도메인 사서 붙이기! ( 가비아에서 구매 ) + Route 53 이용하기

![image](https://github.com/jeon-maker/STUDY_RECORD/assets/77326600/cf9b02f1-0106-4ab9-8acf-a368adb796e6)

[seongcheol.store](http://seongcheol.store) 라는 도메인을 구매하였다 !

![image](https://github.com/jeon-maker/STUDY_RECORD/assets/77326600/f75ee21c-5f05-4c4c-9881-5f133350ed5a)

AWS에서 route 53을 이용하여 내가 구매한 도메인을 연결한다.

먼저 위 사진처럼 호스팅 영역을 구성한다.

- 호스팅 영역 - AWS에서 DNS 레코드를 관리하기 위한 가상의 영역

![image](https://github.com/jeon-maker/STUDY_RECORD/assets/77326600/67c7eb14-10f2-400f-96d8-5b45f0da5af5)

WAS의 Public IP 주소를 DNS에 넣어주었다. 

그 다음 NS 테이블의 주소들을 가비아 내 도메인의 네임서버로 등록해주었다.

![image](https://github.com/jeon-maker/STUDY_RECORD/assets/77326600/d5628513-ca0b-4e20-b7a0-e4ca0d3fb18b)

조금 기다리면 등록이 될 것이다!

![image](https://github.com/jeon-maker/STUDY_RECORD/assets/77326600/1de3018e-4b23-41a3-8b93-add7944469a4)

이제 [seongcheol.store](http://seongcheol.store) 로 접속이 가능하다
