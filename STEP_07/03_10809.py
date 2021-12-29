arr = [-1] * 26
term = input()

cnt = 0
for i in term:
    cnt += 1
    idx = ord(i) - 97
    if arr[idx] == -1:
        arr[idx] += cnt

for i in range(26):
    print(arr[i], end = " ")