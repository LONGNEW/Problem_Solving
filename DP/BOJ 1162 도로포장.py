import sys
from heapq import heappop, heappush

n, m, k = map(int, sys.stdin.readline().split())
graph, distance = [[] for _ in range(n + 1)], [[float('inf')] * (k + 1) for _ in range(n + 1)]

for i in range(k + 1):
    distance[1][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

q = []
heappush(q, (0, k, 1))
while q:
    cost, cnt, node = heappop(q)

    if cost > distance[node][cnt]:
        continue

    for next_cost, next_node in graph[node]:
        if cnt >= 1 and cost < distance[next_node][cnt - 1]:
            distance[next_node][cnt - 1] = cost
            heappush(q, (cost, cnt - 1, next_node))

        if cost + next_cost < distance[next_node][cnt]:
            distance[next_node][cnt] = min(distance[next_node][cnt], cost + next_cost)
            heappush(q, (cost + next_cost, cnt, next_node))

print(min(distance[n]))