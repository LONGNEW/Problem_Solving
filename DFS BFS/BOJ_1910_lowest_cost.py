import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((b, cost))

start, end = map(int, sys.stdin.readline().split())
ans = [float('INF')] * (n + 1)
ans[start] = 0
q = deque([start])

while q:
    now = q.popleft()

    for node, cost in graph[now]:
        if ans[node] > ans[now] + cost:
            ans[node] = ans[now] + cost
            q.append(node)

print(ans[end])
