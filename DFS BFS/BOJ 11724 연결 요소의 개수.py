import sys
from _collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(start):
    q = deque([start])
    visit[start] = True

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visit[i]:
                q.append(i)
                visit[i] = True
    return cnt

visit = [False] * (n + 1)
visit[0] = True
cnt = 0
for i in range(1, n + 1):
    if not visit[i]:
        BFS(i)
        cnt += 1
print(cnt)