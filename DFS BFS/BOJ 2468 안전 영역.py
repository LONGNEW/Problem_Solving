import sys
from collections import deque

def bfs(start_x, start_y, rain):
    q = deque([(start_x, start_y)])
    visit[start_x][start_y] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > rain and visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = 1


n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
for rain in range(101):
    visit = [[0] * n for i in range(n)]
    temp = 0
    for x in range(n):
        for y in range(n):
            if visit[x][y] == 0 and graph[x][y] > rain:
                bfs(x, y, rain)
                temp += 1
    cnt = max(cnt, temp)


print(cnt)