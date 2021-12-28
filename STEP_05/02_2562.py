arr = list()

for i in range(9):
    num = int(input())
    arr.append(num)

max_num = arr[0]
max_idx = 1
for i in range(1, 9):
    if arr[i] > max_num:
        max_num = arr[i]
        max_idx = i+1

print(max_num)
print(max_idx)