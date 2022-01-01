t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    dist = y - x
    total = 0
    gap = 1
    cnt = 0
    flag = True

    while True:
        total += gap
        cnt += 1

        if flag == True:
            flag = False
        else:
            gap += 1
            flag = True

        if dist <= total:
            print(cnt)
            break