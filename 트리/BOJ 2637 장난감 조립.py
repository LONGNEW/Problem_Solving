import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph, value, degree, reverse_degree, nodes = [[] for _ in range(n + 1)], [dict() for _ in range(n + 1)], [0] * (n + 1), [0] * (n + 1), [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[y].append(x)
    value[y][x] = k

    degree[x] += 1
    reverse_degree[y] += 1

q, ans = deque([]), []
for i in range(1, n + 1):
    if not degree[i]:
        nodes[i][i] = 1
        q.append(i)
        ans.append(i)

root = reverse_degree[1:].index(0) + 1
while q:
    node = q.popleft()

    if node == root:
        break

    for next_node in graph[node]:
        degree[next_node] -= 1
        if not degree[next_node]:
            q.append(next_node)

        for i in range(1, n + 1):
            nodes[next_node][i] += value[node][next_node] * nodes[node][i]


for key in ans:
    print(f"{key} {nodes[root][key]}")
