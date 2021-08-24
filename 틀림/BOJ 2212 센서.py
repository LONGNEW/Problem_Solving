import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

temp = []
ans = 0
for i in range(1, n):
    ans += data[i] - data[i - 1]
    heappush(temp, -(data[i] - data[i - 1]))

for i in range(1, k):
    if i >= n:
        break

    ans -= -heappop(temp)

print(ans)