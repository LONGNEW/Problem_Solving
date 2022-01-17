import sys
from heapq import heappop, heappush

def dijkstra(graph):
    q = []
    heappush(q, (0, x))

    dist = [float("inf")] * (n + 1)
    dist[x] = 0

    while q:
        cost, node = heappop(q)

        if cost > dist[node]:
            continue

        for next_cost, next_node in graph[node]:
            temp = next_cost + cost
            if dist[next_node] > temp:
                dist[next_node] = temp
                heappush(q, (temp, next_node))
    return dist

n, m, x = map(int, sys.stdin.readline().split())
original, reverse = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, c = map(int, sys.stdin.readline().split())
    original[u].append((c, v))
    reverse[v].append((c, u))

ori_dist = dijkstra(original)
rev_dist = dijkstra(reverse)
for i in range(n + 1):
    ori_dist[i] += rev_dist[i]

print(max(ori_dist[1:]))