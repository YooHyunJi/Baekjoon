arr = [True for i in range(10001)]
arr[1] = False

for i in range(2, int(10000 ** 0.5) + 1):
    if arr[i] == True:
        gap = 2 * i
        while gap <= 10000:
            arr[gap] = False
            gap += i

cnt = int(input())
for i in range(cnt):
    num = int(input())
    mid = int(num / 2)
    while mid >= 2:
        if arr[mid] == True and arr[num - mid] == True:
            print(mid, num - mid)
            break
        mid -= 1