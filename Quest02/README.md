# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 서원영
- 리뷰어 : 박영준


# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [O] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?
  
- [O] 주석을 보고 작성자의 코드가 이해되었나요?
  > 어렵지만 설명해주셔서 이해를 조금 할 수 있었습니다.
  > 특히 이미지로 탈출하는 길이 나오지 못하지만 행열이 표현되는 것을 확인했습니다
- [X] 코드가 에러를 유발할 가능성이 없나요?
  > 상세한 설명을 해주셨으나 이해가 불가능하여 리뷰로 쓰지 못하였습니다.
- [O] 코드 작성자가 코드를 제대로 이해하고 작성했나요?
  > GPT없이 만드셨다고 하는 것을 듣고 함수에 대한 이해로 쓰셨다는 것을 알게 되었습니다.
- [X] 코드가 간결한가요?
  > 코드가 너무 길고 복잡하여 간결하지 않았습니다.
  > 하지만 배운 커리큘럼의 자료만으로 효율적인 작성은 불가능하다는 것을 이해하고 보았습니다.

# 예시
1. 코드의 작동 방식을 주석으로 기록합니다.
2. 코드의 작동 방식에 대한 개선 방법을 주석으로 기록합니다.
3. 참고한 링크 및 ChatGPT 프롬프트 명령어가 있다면 주석으로 남겨주세요.
```python
# 사칙 연산 계산기
class calculator:
    # 예) init의 역할과 각 매서드의 의미를 서술
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    # 예) 덧셈과 연산 작동 방식에 대한 서술
    def add(self):
        result = self.first + self.second
        return result

a = float(input('첫번째 값을 입력하세요.')) 
b = float(input('두번째 값을 입력하세요.')) 
c = calculator(a, b)
print('덧셈', c.add()) 
```

# 참고 링크 및 코드 개선
```python
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 코드 리뷰를 통해 개선한 코드가 있다면 코드와 간략한 설명을 첨부합니다.
```

