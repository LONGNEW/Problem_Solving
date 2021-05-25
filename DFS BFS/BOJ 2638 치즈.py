import sys
from _collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
sec = 0

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

def BFS():
    # True 이면 내부, False면 외부.
    q = deque([(0, 0)])
    visit = [[False] * M for i in range(N)]
    visit[0][0] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        node_x, node_y = q.popleft()

        for i in range(4):
            nx = node_x + dx[i]
            ny = node_y + dy[i]
            if nx >= N or nx < 0 or ny < 0 or ny >= M:
                continue
            if not visit[nx][ny]:
                if graph[nx][ny]:
                    graph[nx][ny] += 1
                else:
                    visit[nx][ny] = True
                    q.append((nx, ny))



def melt():
    cont = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                cont = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    return cont

temp_cheese = []
while True:
    BFS()
    if melt():
        sec += 1
    else:
        break

print(sec)