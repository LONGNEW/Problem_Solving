import sys
from collections import deque


def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    graph[start_x][start_y] += 1

    cnt = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                cnt += 1
                graph[nx][ny] += 1
                q.append((nx, ny))
    return cnt


m, n, k = map(int, sys.stdin.readline().split())
graph = [[0] * n for i in range(m)]

for i in range(k):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1

ans = []
for x in range(m):
    for y in range(n):
        if graph[x][y] == 0:
            ans.append(bfs(x, y))

print(len(ans))
ans.sort()
for item in ans:
    print(item, end=" ")