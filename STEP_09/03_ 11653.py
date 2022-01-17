num = (int(input()))
div = 2

while num != 1:
    while num % div == 0:
        print(div)
        num /= div
    if div == 2:
        div += 1
    else:
        div += 2