arr = [0] * 10
mul = 1

for i in range(3):
    mul *= int(input())

while mul != 0:
    arr[mul%10] += 1
    mul = mul // 10

for i in range(10):
    print(arr[i])