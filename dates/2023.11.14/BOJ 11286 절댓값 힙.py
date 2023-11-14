from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        if len(data) == 0:
            print(0)
        else:
            _, temp = heappop(data)
            print(temp)
        continue

    heappush(data, (abs(cmd), cmd))
