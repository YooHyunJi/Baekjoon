def hansoo(num):
    # 한자리, 두자리 수는 모두 등차수열
    if num < 100:
        return num
    # 세자리 수 중 가장 작은 한수는 111 -> 110까지는 한자리, 두자리 수의 한수만 존재
    elif num < 111:
        return 99
    else:
        cnt = 99
        for i in range(111, num+1):
            last = i % 10
            middle = (i // 10) % 10
            first = i // 100

            if first - middle == middle - last:
                cnt += 1
        return cnt

print(hansoo(int(input())))