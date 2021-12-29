cnt = int(input())

for i in range(cnt):
    word_new = ''
    repeat, word_origin = input().split()

    for j in word_origin:
        word_new += j * int(repeat)

    print(word_new)