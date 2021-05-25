import sys

n = list(map(int, sys.stdin.readline().strip()))
n.sort(reverse=True)
ret = ''
for i in n:
    ret += str(i)

if int(ret) % 30 == 0:
    print(ret)
else:
    print(-1)