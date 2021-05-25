import sys

w, m, k = map(int, sys.stdin.readline().split())
ret = 0
while w + m >= k and w >= 0 and m >= 0:
    w -= 2
    m -= 1
    ret += 1
print(ret - 1)