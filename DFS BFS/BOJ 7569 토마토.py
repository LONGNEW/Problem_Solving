import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for i in range(n)] for j in range(h)]

q = deque([])
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                q.append((z, x, y, 0))

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
ans = 0

while q:
    z, x, y, day = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
            continue

        if graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = 1
            q.append((nz, nx, ny, day + 1))
    ans = max(ans, day)

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                ans = -1

print(ans)