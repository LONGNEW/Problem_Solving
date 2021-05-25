import sys
from heapq import heappop, heappush

n, k = map(int, sys.stdin.readline().split())
jewel = []
beg = []
capable_jewel = []

for i in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heappush(jewel, (m, v))

for i in range(k):
    c = int(sys.stdin.readline())
    heappush(beg, c)

ans = 0
for i in range(k):
    limit = heappop(beg)

    while jewel and limit >= jewel[0][0]:
        wei, val = heappop(jewel)
        heappush(capable_jewel, (-val, wei))

    if capable_jewel:
        ans -= heappop(capable_jewel)[0]
    elif not jewel:
        break
print(ans)
