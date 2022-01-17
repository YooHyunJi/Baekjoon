from math import dist

num = int(input())

for i in range(num):
    arr = list(map(int, input().split()))
    arr_jo = arr[0:3]
    arr_baek = arr[3:6]
    # 원점간 거리
    dist_center = dist((arr_jo[0], arr_jo[1]), (arr_baek[0], arr_baek[1]))
    # ((arr_jo[0] - arr_baek[0]) ** 2 + (arr_jo[1] - arr_baek[1]) ** 2) ** 0.5
    # 반지름 차
    dist_minus = abs(arr_jo[2] - arr_baek[2])
    # 반지름 합
    dist_plus = arr_jo[2] + arr_baek[2]

    if arr_jo == arr_baek:
        status = -1
    elif dist_center > dist_plus or dist_center < dist_minus:
        status = 0
    elif dist_center == dist_plus or dist_center == dist_minus:
        status = 1
    elif dist_center < dist_plus:
        status = 2
    
    print(status)