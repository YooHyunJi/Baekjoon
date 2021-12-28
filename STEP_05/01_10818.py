num = int(input())
arr = list(map(int, input().split()))
minimum = arr[0]
maximum = arr[0]

for i in range(1, num):
    if arr[i] < minimum:
        minimum = arr[i]
    if arr[i] > maximum:
        maximum = arr[i]
print(minimum, maximum)