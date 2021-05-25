import sys

n, k = map(int, sys.stdin.readline().split())
data = [i for i in range(1, n + 1)]

res = []
idx = k - 1
for i in range(n):
    if idx >= len(data):
        idx %= len(data)
        res.append(data.pop(idx))
        idx += k - 1
    else:
        res.append(data.pop(idx))
        idx += k - 1
print("<", end="")
for idx, item in enumerate(res):
    if idx == len(res) - 1:
        print(item, end="")
    else:
        print("{}, ".format(item), end="")
print(">")

----------------------------------------------------------------
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, N + 1)])
res = []

while q:
    q.rotate(-K+1)
    res.append(str(q.popleft()))

sys.stdout.write("<"+", ".join(res)+">")
