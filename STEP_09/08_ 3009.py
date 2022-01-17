x = [0] * 3
y = [0] * 3

for i in range(3):
    x[i], y[i] = map(int, input().split())

if x[0] == x[1]:
    x_new = x[2]
else:
    if x[0] == x[2]:
        x_new = x[1]
    else:
        x_new = x[0]

if y[0] == y[1]:
    y_new = y[2]
else:
    if y[0] == y[2]:
        y_new = y[1]
    else:
        y_new = y[0]

print(x_new, y_new)