x, y, w, h  = map(int, input().split())
arr = [0] * 4

arr[0] = x
arr[1] = y
arr[2] = w - x
arr[3] = h - y

print(min(arr))