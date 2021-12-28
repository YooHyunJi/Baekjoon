num = int(input())

for i in range(num):
    keep = 0
    score = 0
    arr = input()

    for j in arr:
        if j == 'O':
            keep += 1
        else:
            keep = 0
        score += keep

    print(score)