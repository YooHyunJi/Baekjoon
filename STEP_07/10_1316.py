num = int(input())
group = 0

for i in range(num):
    cnt = 0
    compare = 'A'
    word = input()

    for j in word:
        if j != compare:
            cnt += 1
            compare = j

    if cnt == len(set(word)):
        group += 1
    
print(group)