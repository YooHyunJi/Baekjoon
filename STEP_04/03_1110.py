import math

num_origin = int(input())
num_new = num_origin
cnt = 0

while True:
    cnt += 1
    num_sum = math.trunc(num_new/10) + num_new%10
    num_new = (num_new%10 * 10) + (num_sum%10)
    if num_new == num_origin:
        break
print(cnt)