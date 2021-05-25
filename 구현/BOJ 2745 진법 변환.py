import sys

n, b = sys.stdin.readline().split()
b = int(b)
res = 0

for idx, item in enumerate(n):
    try:
        if int(item):
            res += int(item) * b ** (len(n) - 1 - idx)
    except:
        res += (ord(item) - 55) * b ** (len(n) - 1 - idx)
print(res)