cnt = int(input())

for i in range(1, cnt+1):
    star = " " * (cnt-i) + "*" * i
    print(star)