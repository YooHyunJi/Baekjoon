t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    arr_origin = [0] * n
    arr_new = [0] * n

    for j in range(n):
        arr_origin[j] = j + 1

    for j in range(k):
        for l in range(n):
            arr_new[l] = sum(arr_origin[0 : l+1])
        arr_origin = arr_new.copy()

    print(arr_origin[n - 1])