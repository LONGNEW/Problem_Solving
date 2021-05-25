import sys
import heapq

n = int(sys.stdin.readline())
data = []
for i in range(n):
    s, t = map(int, sys.stdin.readline().split())
    data.append((s, t))

data.sort(key=lambda x:(x[0], x[1]))
q = []
heapq.heappush(q, data[0][1])

for i in range(1, n):
    time = q[0]
    if time > data[i][0]:
        heapq.heappush(q, data[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, data[i][1])

print(len(q))