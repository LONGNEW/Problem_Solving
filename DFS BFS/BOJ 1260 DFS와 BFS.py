import sys
from _collections import deque
n, m, v= map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

def DFS(start):
    visit[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visit[i]:
            DFS(i)

def BFS(start):
    q = deque([start])
    visit[start] = True

    while q:
        now = q.popleft()
        print(now, end=" ")

        for i in graph[now]:
            if not visit[i]:
                q.append(i)
                visit[i] = True


visit = [False] * (n + 1)
DFS(v)
print()
visit = [False] * (n + 1)
BFS(v)