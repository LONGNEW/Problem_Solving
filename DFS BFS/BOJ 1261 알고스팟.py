import sys
from _collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))
visit = [[99999] * m for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque([])
    q.append((0, 0))
    visit[0][0] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            # 다음 이동하는 곳에 벽이 존재.
            if graph[nx][ny] == 1:
                if visit[nx][ny] == 99999 or visit[nx][ny] > visit[x][y] + 1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
            else:
                if visit[nx][ny] == 99999 or visit[nx][ny] > visit[x][y]:
                    visit[nx][ny] = min(visit[nx][ny], visit[x][y])
                    q. append((nx, ny))

bfs()
print(visit[n - 1][m - 1])

