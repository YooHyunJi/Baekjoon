num = int(input())

for i in range(num):
    avg = 0
    cnt = 0

    arr = list(map(int, input().split()))
    avg = (sum(arr[1:]) / arr[0])
    
    for j in range(1, arr[0]+1):
        if arr[j] > avg:
            cnt += 1
    
    print("{:.3f}%".format(cnt / arr[0] * 100))