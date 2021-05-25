import sys
from _collections import deque

n = int(sys.stdin.readline())
rectangle = []
for i in range(n):
    rectangle.append(list(map(int, sys.stdin.readline().split())))

graph = [[0] * 2001 for i in range(2001)]
position = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 0, 0 은 1000, 1000
for item in rectangle:
    x1 = 2 * (500 + item[0])
    y1 = 2 * (500 + item[1])
    x2 = 2 * (500 + item[2])
    y2 = 2 * (500 + item[3])

    position.append((x1, y1))
    for nx in range(x1, x2 + 1):
        if nx == x1 or nx == x2:
            for ny in range(y1, y2 + 1):
                graph[nx][ny] = 1
        else:
            graph[nx][y1] = 1
            graph[nx][y2] = 1


def bfs(x, y):
    q = deque([])
    q.append((x, y))
    graph[x][y] = 0

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx > 2000 or nx < 0 or ny > 2000 or ny < 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


if graph[1000][1000] == 1:
    cnt = -1
else:
    cnt = 0
for x, y in position:
    if graph[x][y] == 1:
        cnt += 1
        bfs(x, y)

print(cnt)