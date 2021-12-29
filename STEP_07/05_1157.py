# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90
# 대문자 + 32 = 소문자

# 단어 입력
word = input()
arr = [0] * 26

# 알파벳 개수 카운트, 소문자일 경우 대문자로 카운트
for i in word:
    if i >= 'a' and i <= 'z':
        idx = ord(i) - 32
    else:
        idx = ord(i)
    arr[idx - 65] += 1

# 가장 많이 나온 알파벳 탐색
max_num = 0
max_idx = 0
cnt = 0
for i in range(26):
    # 현 최대 빈도수보다 자주 나온 알파벳을 찾았을 때
    if arr[i] > max_num:
        max_num = arr[i]
        max_idx = i
        cnt = 1
    # 현 최대 빈도수만큼 나온 알파벳을 찾았을 때
    elif arr[i] == max_num:
        cnt += 1

# 최대 빈도수만큼 나온 알파벳이 하나가 아닐 때
if cnt != 1:
    print("?")
# 최대 빈도수만큼 나온 알파벳이 하나일 때
else:
    print(chr(max_idx + 65))
