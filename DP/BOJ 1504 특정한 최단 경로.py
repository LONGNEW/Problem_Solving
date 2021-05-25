import sys
import heapq

n, e = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    ret = [999999] * (n + 1)
    ret[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, now = heapq.heappop(q)

        if cost > ret[now]:
            continue

        for next_node, next_cost in graph[now]:

            total_cost = next_cost + cost

            if ret[next_node] > total_cost:
                ret[next_node] = total_cost
                heapq.heappush(q, (total_cost, next_node))
    return ret

one = dijkstra(1)
list_v1 = dijkstra(v1)
list_v2 = dijkstra(v2)
ret = min(one[v1] + list_v1[v2] + list_v2[n], one[v2] + list_v2[v1] + list_v1[n])
if ret < 999999:
    print(ret)
else:
    print(-1)