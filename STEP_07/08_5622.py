word = input()
num = []

# 알파벳 연락처를 숫자 연락처로 변환
for i in word:
    if 'A' <= i and i <= 'C':
        num.append(1)
    elif 'D' <= i and i <= 'F':
        num.append(2)
    elif 'G' <= i and i <= 'I':
        num.append(3)
    elif 'J' <= i and i <= 'L':
        num.append(4)
    elif 'M' <= i and i <= 'O':
        num.append(5)
    elif 'P' <= i and i <= 'S':
        num.append(6)
    elif 'T' <= i and i <= 'V':
        num.append(7)
    elif 'W' <= i and i <= 'Z':
        num.append(8)

time = len(num) * 2 + sum(num)
print(time)