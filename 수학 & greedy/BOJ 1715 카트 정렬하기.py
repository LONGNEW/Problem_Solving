import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
data = []
for i in range(n):
    temp = int(sys.stdin.readline())
    heappush(data, temp)

ans = 0
while len(data) > 1:
    a = heappop(data)
    b = heappop(data)
    ans += a + b
    heappush(data, a + b)

print(ans)