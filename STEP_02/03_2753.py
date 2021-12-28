year = int(input())
flag = 0

if year % 4 == 0:
    if year % 100 != 0:
        flag = 1
    elif year % 400 == 0:
        flag = 1

if flag == 1:
    print("1")
else:
    print("0")