num = int(input())
arr = list(map(int, input().split()))

max_score = arr[0]
sum_score = arr[0]
for i in range(1, num):
    sum_score += arr[i]
    if arr[i] > max_score:
        max_score = arr[i]

print((sum_score / num) / max_score * 100)