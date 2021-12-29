sentence = input()

# 일반적인 문장에서 단어의 개수 : 공백 개수 + 1 -> 공백 개수 카운트
cnt = 0
for i in sentence:
    if i == ' ':
        cnt += 1

# 맨 앞 or 맨 뒤에 있는 공백은 단어의 개수에 영향을 미치치 않음
exception = 0
if sentence[0] == ' ':
    exception += 1
if sentence[-1] == ' ':
    exception += 1

print(cnt - exception + 1)