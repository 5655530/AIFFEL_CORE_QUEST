# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 서원영
- 리뷰어 : 심지안


# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [V] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?  
  코드가 의도한 대로 정상적으로 동작했습니다. 특히 추출적 요약 부분에서 막혔었는데 배워가게되었습니다
- [V] 주석을 보고 작성자의 코드가 이해되었나요?
  > 대부분 이해 되었습니다
- [V] 코드가 에러를 유발할 가능성이 없나요?
  > 없는 것 같습니다
- [V] 코드 작성자가 코드를 제대로 이해하고 작성했나요?
  > 그런 것 같습니다
- [V] 코드가 간결한가요?
  > 필요한 코드들로만 작성된 것 같습니다

# 예시
```python
# 데이터 로드
data = pd.read_csv('news_summary_more.csv', encoding='iso-8859-1')

# 'text' 열에서 데이터를 추출적 요약하여 출력
for idx, text in enumerate(data['text']):
    print(f"Original Text {idx + 1}:\n{text}\n")
    print(f"Summarized Text {idx + 1}:\n{summarize(text, ratio=0.5)}\n")
    print("-"*100)

    if idx == 4:
        break

# 요약문이 아닌 원문에서 데이터를 가져와 summarize시켜야 잘 작동됨을 알게되었습니다
```

# 참고 링크 및 코드 개선
