def re_hanoi(num, start, middle, end):
    if num == 1:
        print(start, end)
    else:
        re_hanoi(num-1, start, end, middle)
        print(start, end)
        re_hanoi(num-1, middle, start, end)

num = int(input())

print(2 ** num - 1)
re_hanoi(num, 1, 2, 3)