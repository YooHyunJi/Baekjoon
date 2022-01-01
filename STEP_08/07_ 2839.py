num = int(input())
rest = num
quan_3 = 0
quan_5 = 0
flag = True

for i in range(num // 3 + 1):
    if rest % 5 == 0:
        quan_5 = rest // 5
        break
    else:
        quan_3 += 1
        rest -=3
        if 0 < rest < 3:
            flag = False

if flag == False:
    total = -1
else:
    total = quan_3 + quan_5

print(total)