import sys
from _collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
cache = [[[0] * 2 for _ in range(M)] for _ in range(N)]

for i in range(N):
    data = sys.stdin.readline().strip()
    for j in data:
        graph[i].append(int(j))

def BFS():
    q = deque([(0, 0, 1)])
    cache[0][0][1] = 1

    while q:
        x, y, crash = q.popleft()
        if x == N - 1 and y == M - 1:
            return cache[N - 1][M - 1][crash]
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if graph[nx][ny]:
                if crash and not cache[nx][ny][crash - 1]:
                    cache[nx][ny][crash - 1] = cache[x][y][crash] + 1
                    q.append((nx, ny, crash - 1))
                else:
                    continue
            else:
                if not cache[nx][ny][crash]:
                    cache[nx][ny][crash] = cache[x][y][crash] + 1
                    q.append((nx, ny, crash))
ret = BFS()
if ret:
    print(ret)
else:
    print(-1)