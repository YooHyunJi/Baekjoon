arr = [0] * 10001

def selfNumber(num_input):
    num_sum = num_input
    while num_input != 0:
        num_sum += num_input % 10
        num_input = num_input // 10
    return num_sum

for i in range(1, 10001):
    if arr[i] == 0:
        num = selfNumber(i)
        while num <= 10000:
            arr[num] += 1
            num = selfNumber(num)

for i in range(1, 10001):
    if arr[i] == 0:
        print(i)

## 처음에 시도한 방법
# def selfNumber(num_input):
#     flag = 0
#     for i in range(1, num_input):
#         num_tmp = i
#         num_sum = i

#         while num_tmp != 0:
#             num_sum += num_tmp % 10
#             num_tmp = num_tmp // 10

#         if num_sum == num_input:
#             flag = 1
#             break

#         if flag == 1:
#             return 1
#     if flag == 0:
#         return 0

# for i in range(10000):
#     if selfNumber(i+1) == 0:
#         print(i+1)