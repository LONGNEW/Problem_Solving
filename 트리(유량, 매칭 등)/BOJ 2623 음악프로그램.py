import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
node, graph = [0] * (n + 1), [[] for _ in range(n + 1)]

for _ in range(m):
    edge = list(map(int, sys.stdin.readline().split()))[1:]
    for idx in range(len(edge) - 1):
        now, daum = edge[idx], edge[idx + 1]
        graph[now].append(daum)
        node[daum] += 1

q = deque([])
for i in range(1, n + 1):
    if node[i] == 0:
        q.append(i)

ans = []
while q:
    now = q.popleft()
    ans.append(now)

    for next_node in graph[now]:
        node[next_node] -= 1
        if node[next_node] == 0:
            q.append(next_node)

if sum(node) != 0:
    print(0)
    exit(0)

for item in ans:
    print(item)