import sys
import heapq

inf = 100000000

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v + 1)]
dp = [inf] * (v + 1)
heap = []


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, node = heapq.heappop(heap)

        for next_node, next_weight in graph[node]:
            total = next_weight + weight

            if total < dp[next_node]:
                dp[next_node] = total
                heapq.heappush(heap, (dp[next_node], next_node))


for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dijkstra(k)

for i in dp[1:]:
    if i != inf:
        print(i)
    else:
        print("INF")