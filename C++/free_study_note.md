# unorderd_map 
  - ![image](https://user-images.githubusercontent.com/77326600/228415762-c85d8259-59ed-40a9-be16-566c75fb3759.png)
  - key-value 쌍으로 묶여진 map이다. 정렬이 되어있지 않으며 key값으로 빠르게 검색할 수 있다/
  - 위 사진처럼 실행하면 1이 출력된다
  - ![image](https://user-images.githubusercontent.com/77326600/228416014-6687e301-8202-44a2-b0d6-ba11dbe9cfbf.png)
  - 위 사진처럼 없는 값을 검색해도 에러가 발생하지 않고 0이 출력된다.
  - **key-value 조합에서 빠르게 key 값으로 찾을 수 있을 것 같다**
  
 
 
 # 참조자 & 와 auto
  - ![image](https://user-images.githubusercontent.com/77326600/228481801-5567b170-7622-4530-953a-0724b14112b8.png)
  -  참조자 & : 변수를 담은 주소값 .
      - 참조자는 변수를 참조할 수 있고, 데이터 값만은 참조할 수 없음
      - 어떤 한 변수의 참조자가 되어버리면 더이상 다른 변수를 참조할 수 없게 됨
  - auto : 추론 가능한 형식의 타입을 반환함
  - 따라서 위 코드는 모두 11, 12를 출력함
  
#iterator : 포인터처럼 쓰임
 - map<key,value> 에서 쓰일때 it-> first :key, it->second : value
 
# Map

map의 원소들은 key 값을 기준으로 오름차순 정렬되어있다,

key값을 기준으로 내림차순 정렬하고 싶으면 int형 기준으로

map<int,int,greater>를 사용해주면 된다

### key가 아니라 value 로 정렬?!

- map 을 vector로 옮겨서 정렬해야함.
- map → vector
- sort vector



 


