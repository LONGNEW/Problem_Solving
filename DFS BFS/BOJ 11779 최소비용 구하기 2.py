import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
prev_node, distance = [-1] * (n + 1), [float("inf")] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))

start, end = map(int, sys.stdin.readline().split())
q = []
heappush(q, (0, start))
distance[start] = 0

while q:
    now_dist, now_node = heappop(q)

    if distance[now_node] < now_dist:
        continue

    for cost, next_node in graph[now_node]:
        if now_dist + cost < distance[next_node]:
            heappush(q, (now_dist + cost, next_node))
            distance[next_node] = now_dist + cost
            prev_node[next_node] = now_node

route = [end]
now_node = end
while now_node != start:
    now_node = prev_node[now_node]
    route.append(now_node)
route.reverse()

print(distance[end])
print(len(route))
print(*route)
