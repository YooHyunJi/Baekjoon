m, n = map(int, input().split())
arr = [True for i in range(n+1)]
arr[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if arr[i] == True:
        gap = i * 2
        while gap <= n:
            arr[gap] = False
            gap += i

for i in range(m, n+1):
    if arr[i] == True:
        print(i)