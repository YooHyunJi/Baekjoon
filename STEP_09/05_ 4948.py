arr = [True for i in range(2 * 123456 + 1)]
arr[1] = False

for i in range(2, int((2 * 123456) ** 0.5) + 1):
    if arr[i] == True:
        gap = i * 2
        while gap <= 2 * 123456:
            arr[gap] = False
            gap += i

while True:
    num = int(input())

    if num == 0:
        break
    else:
        print(arr[num + 1 : 2 * num + 1].count(True))