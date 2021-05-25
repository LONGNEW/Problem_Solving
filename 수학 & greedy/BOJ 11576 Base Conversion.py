import sys

n, m = map(int, sys.stdin.readline().split())
cnt = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

data = 0
idx = 0
for i in range(cnt - 1, -1, -1):
    data += num[idx] * (n ** i)
    idx += 1

ret = []
while data != 0:
    ret.append(data % m)
    data //= m
    
ret.reverse()
for item in ret:
    print(item, end=" ")