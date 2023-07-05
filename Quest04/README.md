# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 코더 1인의 이름을 작성하세요.
- 리뷰어 : 본인의 이름을 작성하세요.


# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [X] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?
  
- [X] 주석을 보고 작성자의 코드가 이해되었나요?
  > 해당 코드들이 각각 어떤 기능을 하는지, 기능별로 주석으로 구체적으로 명시되어있어 이해하기 수월했습니다.
- [X] 코드가 에러를 유발할 가능성이 없나요?
  > gen_result 사용: 제네레이터를 사용하여 결과를 출력할 때, 마지막 for 루프에서 compre_result 대신gen_result`를 사용해야 합니다.
  > 아래 참고 링크 및 코드 개선에 수정 코드 참고해주세요.
- [X] 코드 작성자가 코드를 제대로 이해하고 작성했나요?
  > 각 코드의 기능을 잘 설명하여 모든 부분을 이해하고 작성한 것으로 보입니다.
- [X] 코드가 간결한가요?
  > 위 항목에 대한 근거 작성 필수

# 예시
1. 코드의 작동 방식을 주석으로 기록합니다.
2. 코드의 작동 방식에 대한 개선 방법을 주석으로 기록합니다.
3. 참고한 링크 및 ChatGPT 프롬프트 명령어가 있다면 주석으로 남겨주세요.
```python
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
import time

# fish_compre 함수: 리스트 컴프리헨션을 사용하여 생선리스트에서 각 생선의 설명을 생성합니다.
def fish_compre(fish_list):
    return [f"{fish['이름']} is swimming at {fish['speed']} m/s" for fish in fish_list]

# fish_gen 함수: 제너레이터를 사용하여 생선리스트에서 각 생선의 설명을 생성합니다.
def fish_gen(fish_list):
    for fish in fish_list:
        yield f"{fish['이름']} is swimming at {fish['speed']} m/s"

# 예시 생선 리스트
fish_list = [
    {"이름": "Nemo", "speed": 3},
    {"이름": "Dory", "speed": 5},
]

# 리스트 컴프리헨션 사용 예제 출력
print("Using Comprehension:")
compre_result = fish_compre(fish_list)
for result in compre_result:
    print(result)
    time.sleep(2)  # 2초마다 결과 출력

# 제너레이터 사용 예제 출력
print("Using Generator:")
gen_result = fish_gen(fish_list)
for result in gen_result:  # 'gen_result'를 사용하여 결과 출력
    print(result)
    time.sleep(2)  # 2초마다 결과 출력

```
01. 함수 이름: 함수 이름이 더 의미 있는 이름으로 변경되면 좋겠습니다. 예를 들어, fish_compre을 주석: 주석 동작 및 함수에 대한 설명이 명확해야 합니다. 완전한 주석은 코드를 이해하는데 도움이 됩니다.
02. gen_result 사용: 제네레이터를 사용하여 결과를 출력할 때, 마지막 for 루프에서 compre_result 대신gen_result`를 사용해야 합니다.
03. 아래와 같이 주어진 코드를 더 짧게 작성하기 위해 다음과 같이 수정할 수 있습니다
   
두 개의 함수를 삭제하고 리스트 컴프리헨션 및 제너레이터 식을 바로 사용합니다.  

모든 결과를 출력하는 데 사용되는 for 루프를 minimize하여 두 개의 출력 모드에 중복을 줄입니다.  

이제 간결하게 작성된 코드를 확인해 보세요.

```python
import time

fish_list = [
    {"이름": "Nemo", "speed": 3},
    {"이름": "Dory", "speed": 5},
]

def print_result(mode, result_iterator):
    print(f"Using {mode}:")
    for result in result_iterator:
        print(result)
        time.sleep(2)

compre_result = [f"{fish['이름']} is swimming at {fish['speed']} m/s" for fish in fish_list]
print_result("Comprehension", compre_result)

gen_result = (f"{fish['이름']} is swimming at {fish['speed']} m/s" for fish in fish_list)
print_result("Generator", gen_result)
```
