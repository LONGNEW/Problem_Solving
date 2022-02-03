import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans, cnt = float("inf"), float("inf")
for i in range(1, n + 1):
    visit, temp = [0] * (n + 1), 0
    q = deque([(i, 0)])
    visit[i] = 1

    while q:
        node, move = q.popleft()
        temp += move

        for next_node in graph[node]:
            if visit[next_node]:
                continue
            visit[next_node] = 1
            q.append((next_node, move + 1))

    if cnt > temp:
        ans, cnt = i, temp

print(ans)