arr = list()

for i in range(10):
    arr.append(int(input()) % 42)

cnt = 1
for i in range(1, 10):
    flag = 0
    for j in range(i):
        if arr[i] == arr[j]:
            flag = 1
            break
    if flag == 0:
        cnt += 1

print(cnt)