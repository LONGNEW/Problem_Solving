import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
parent = [0] + list(map(int, sys.stdin.readline().split()))
ans, graph, value = [0] * (n + 1), [[] for _ in range(n + 1)], dict()

for i in range(2, n + 1):
    graph[parent[i]].append(i)

for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())

    if i not in value:
        value[i] = w
    else:
        value[i] += w

q = deque([(0, 1)])
while q:
    cost, node = q.popleft()
    ans[node] = cost

    for next_node in graph[node]:
        temp = 0

        if next_node in value:
            temp += value[next_node]
        q.append((cost + temp, next_node))

print(*ans[1:])