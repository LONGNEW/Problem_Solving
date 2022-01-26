import sys

n = int(sys.stdin.readline())
cnt, prev = 0, 0

for i in range(1, 1000):
    prev = cnt
    cnt += i
    if cnt >= n:
        break

up, down = i, 1
for i in range(n - prev - 1):
    up -= 1
    down += 1

print(up, down)