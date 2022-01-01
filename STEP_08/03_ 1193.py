num = int(input())
total = 1
step = 1

while True:
    if num <= total:
        gap = total - num
        if step % 2 == 1:
            a = 1 + gap
            b = step - gap
        else:
            a = step - gap
            b = 1 + gap
        break
    step += 1
    total += step

print("{}/{}".format(a, b))