def re_factorial(num):
    while True:
        if num == 0:
            return 1
        else:
            return num * re_factorial(num-1)

num = int(input())

print(re_factorial(num))