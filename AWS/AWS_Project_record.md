# Architecture 

## 1. Down Time이 없는 인프라를 위해서 다음과 같이 아키텍처를 구성해봤습니다.
### 이관하는 동안의 아키텍처
![image](https://user-images.githubusercontent.com/77326600/230461480-266a91b0-dc5f-4824-9937-e2a2ece09847.png)

핵심 포인트는 ALB 입니다.
ALB를 통해서 On-Premise 서버, AWS EC2 에 접근할 수 있습니다.
데이터를 이관하는 동안 On-Premise 서버를 통해 서비스를 유지하며 AWS EC2에 이관하는 방식의 구조입다.
또는 하이브리드 클라우드 방식을 택하여 기존 On-Premise 서버를 유지하며 클라우드 서비스를 이용하는 방식으로 운영하는 것도 하나의 방법이 될 것입니다.

![image](https://user-images.githubusercontent.com/77326600/230462244-99ca6d11-e211-4380-948d-5d9fe2ae4ed5.png
위처럼 URL을 통해서 대상 그룹에 접근할 수 있는데, 대규모 프로모션 기간에는 행사 상품의 URL을 따로 설정하여 대상 그룹을 만드는 방식도 고려할 수 있을 것 같습니다.
(그렇게 되면 결제 단계에서 결국 합쳐지게 될텐데, 이때는 회원 ID를 쿼리로 하여 또 대상 그룹을 유연하게 묶을 수 있을 것 같습니다.)


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
