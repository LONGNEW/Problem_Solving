import sys
from _collections import deque

N, M = map(int, sys.stdin.readline().split())
Hx, Hy = map(int, sys.stdin.readline().split())
Ex, Ey = map(int, sys.stdin.readline().split())
graph = [[-1] * (M + 1) for _ in range(N + 1)]
cache = [[[0] * 2 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(len(data)):
        graph[i][j + 1] = data[j]

def BFS():
    q = deque([(Hx, Hy, 1)])
    cache[Hx][Hy][1] = 1

    while q:
        x, y, crash = q.popleft()
        if x == Ex and y == Ey:
            return cache[x][y][crash]
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > N or nx < 1 or ny > M or ny < 1:
                continue
            if graph[nx][ny] == 1:
                if crash and not cache[nx][ny][crash - 1]:
                    cache[nx][ny][crash - 1] = cache[x][y][crash] + 1
                    q.append((nx, ny, crash - 1))
                else:
                    continue
            elif graph[nx][ny] == 0:
                if not cache[nx][ny][crash]:
                    cache[nx][ny][crash] = cache[x][y][crash] + 1
                    q.append((nx, ny, crash))
ret = BFS()
if ret:
    print(ret - 1)
else:
    print(-1)