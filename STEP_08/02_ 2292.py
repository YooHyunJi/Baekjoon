num = int(input())
limit = 1
step = 1

while True:
    if num <= limit:
        print(step)
        break
    else:
        limit += 6 * step
        step += 1