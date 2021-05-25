import sys
n, m = map(int, sys.stdin.readline().split())
ret = 1
if n == 2:
    ret = min(4, (m + 1) // 2)
elif n >= 3:
    if m <= 6:
        ret = min(4, m)
    else:
        ret = m - 2
print(ret)
