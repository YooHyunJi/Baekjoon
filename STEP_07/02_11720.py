cnt = int(input())
arr = input()

total = 0

# # 방법 1
# for i in range(cnt):
#     total += int(arr[i])

# 방법 2
for i in arr:
    total += int(i)

print(total)
