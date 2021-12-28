n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    num = a[i]
    if num < x:
        print(num, end=" ")