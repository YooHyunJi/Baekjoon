cnt = int(input())

for i in range(cnt):
    a, b = map(int, input().split())
    print("Case #{}: {}".format(i+1, a+b))