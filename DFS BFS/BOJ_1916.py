import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b, c = (map(int, sys.stdin.readline().split()))
    graph[a].append((b, c))

dist = [float('inf')] * (n + 1)
start, end = map(int, sys.stdin.readline().split())
dist[start] = 0
q = [(0, start)]

while q:
    now_cost, now_node = heappop(q)

    if dist[now_node] < now_cost:
        continue

    for next_node, next_cost in graph[now_node]:
        cost = now_cost + next_cost
        if dist[next_node] > cost:
            dist[next_node] = cost
            heappush(q, (cost, next_node))
print(dist[end])