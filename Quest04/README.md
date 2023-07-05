# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 코더 1인의 이름을 작성하세요.
- 리뷰어 : 본인의 이름을 작성하세요.


# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [X] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?
  
- [X] 주석을 보고 작성자의 코드가 이해되었나요?
  > 해당 코드들이 각각 어떤 기능을 하는지, 기능별로 주석으로 구체적으로 명시되어있어 이해하기 수월했다.
- [X] 코드가 에러를 유발할 가능성이 없나요?
  >위 항목에 대한 근거 작성 필수
- [X] 코드 작성자가 코드를 제대로 이해하고 작성했나요?
  > 위 항목에 대한 근거 작성 필수
- [X] 코드가 간결한가요?
  > 위 항목에 대한 근거 작성 필수

# 예시
1. 코드의 작동 방식을 주석으로 기록합니다.
2. 코드의 작동 방식에 대한 개선 방법을 주석으로 기록합니다.
3. 참고한 링크 및 ChatGPT 프롬프트 명령어가 있다면 주석으로 남겨주세요.
```python
# 사칙 연산 계산기
import time #sleep함수 이용하기 위해 import

def fish_compre(fish_list) : #생선리스트 컴프리헨션으로 출력하는 함수 생성
  return [f"{fish['이름']} is swimming at {fish['speed']} m/s" for fish in fish_list]

def fish_gen(fish_list) : #생선리스트 제너레이터로 출력하는 함수 생성
  for fish in fish_list:
    yield f"{fish['이름']} is swimming at {fish['speed']} m/s"


fish_list = [
{"이름": "Nemo", "speed": 3},
{"이름": "Dory", "speed": 5},
] #생선리스트 생선

print("Using Comprehension:")
compre_result =fish_compre(fish_list) #fish_compre함수 호출
for result in compre_result : #생선 리스트 컴프리헨션으로 출력
    print(result)
    time.sleep(2) #2초 간격으로 출력

print("Using  Generator:")
gen_result =fish_gen(fish_list) #fish_gen함수 호출
for result in compre_result : #생선 리스트 제너레이터로 출력
    print(result)
    time.sleep(2) #2초 간격으로 출력
```


# 참고 링크 및 코드 개선
```python
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 코드 리뷰를 통해 개선한 코드가 있다면 코드와 간략한 설명을 첨부합니다.
```
함수 이름: 함수 이름이 더 의미 있는 이름으로 변경되면 좋겠습니다. 예를 들어, fish_compre을 describe_fish_with_comprehension, fish_gen을 describe_fish_with_generator로 변경합니다.  

사용자 입력 처리: 사용자 입력을 좀 더 효율적으로 처리하기 위해, list 대신에 zip으로 이름과 속도를 짝지어 저장하도록 합니다. 

gen_result 출력: 제너레이터를 사용하여 출력할 때, compre_result 대신 gen_result를 사용합니다.  
