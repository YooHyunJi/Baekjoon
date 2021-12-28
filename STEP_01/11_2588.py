import math

a = int(input())
b = int(input())

# (6)
mul_final = (a * b)

# (3)
mul = b % 10
print(a * mul)

# (4)
b = math.trunc(b / 10)
mul = b % 10
print(a * mul)

# (5)
b = math.trunc(b / 10)
mul = b % 10
print(a * mul)

print(mul_final)