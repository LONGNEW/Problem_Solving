import sys
from _collections import deque

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs(start):
    q = deque([start])

    while q:
        now = q.popleft()
        for i in range(n):
            if graph[now][i] == 1 and visit[i] == 0:
                q.append(i)
                visit[i] = 1
                graph[start][i] = 1

for i in range(n):
    visit = [0] * n
    bfs(i)

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()