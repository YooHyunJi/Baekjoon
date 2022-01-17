def isDecimal(x):
    # 1은 소수가 아님
    if x == 1:
        return False
    
    # 2는 소수
    elif x == 2:
        return True
    
    # 2가 아닌 짝수는 소수가 아님
    elif x % 2 == 0:
        return False

    # 1이 아닌 홀수에 대해 소수 판별
    else:   
        cnt = 0
        for i in range(1, x+1):
            if x % i == 0:
                cnt += 1
            if cnt > 2:
                return False

        if cnt == 2:
            return True

m = int(input())
n = int(input())
arr = []

for i in range(m, n+1):
    if isDecimal(i) == True:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print("{}\n{}".format(sum(arr), min(arr)))