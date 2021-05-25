import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
ret = 0
for i in range(n):
    coin.append(int(sys.stdin.readline()))

for i in range(n - 1, -1, -1):
    if k // coin[i] >= 1:
        ret += k // coin[i]
        k %= coin[i]

print(ret)