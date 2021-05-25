import sys
from _collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    data = list(sys.stdin.readline().split())
    graph.append(data)
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            q.append((i, j, 0))

while q:
    x, y, day = q.popleft()
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if graph[nx][ny] == '0':
            graph[nx][ny] = '1'
            q.append((nx, ny, day + 1))

total = m * n
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            cnt += 1
        elif graph[i][j] == '-1':
            total -= 1
if cnt == total:
    print(day)
elif cnt < total:
    print(-1)