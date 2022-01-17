def isDecimal(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False

num = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in range(num):
    if isDecimal(arr[i]) == True:
        cnt += 1

print(cnt)