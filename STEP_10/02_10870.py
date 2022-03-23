def re_fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return re_fibonacci(num-1) + re_fibonacci(num-2)

num = int(input())

print(re_fibonacci(num))