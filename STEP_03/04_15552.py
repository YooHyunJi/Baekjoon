import sys

input = sys.stdin.readline
cnt = int(input())

for i in range(cnt):
    a, b = map(int, input().split())
    print(a + b)