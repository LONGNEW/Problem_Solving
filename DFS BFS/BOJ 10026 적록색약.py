import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_rb(pos_x, pos_y, target):
    q = deque([])
    visit[pos_x][pos_y] = 1
    q.append((pos_x, pos_y))

    while q:
        pos_x, pos_y = q.popleft()

        for j in range(4):
            nx = pos_x + dx[j]
            ny = pos_y + dy[j]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if target == 'R' or target == 'G':
                if visit[nx][ny] == 0 and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                    q.append((nx, ny))
                    visit[nx][ny] = 1
            else:
                if visit[nx][ny] == 0 and graph[nx][ny] == 'B':
                    q.append((nx, ny))
                    visit[nx][ny] = 1


def bfs(pos_x, pos_y, target):
    q = deque([])
    visit[pos_x][pos_y] = 1
    q.append((pos_x, pos_y))

    while q:
        pos_x, pos_y = q.popleft()

        for j in range(4):
            nx = pos_x + dx[j]
            ny = pos_y + dy[j]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visit[nx][ny] == 0 and graph[nx][ny] == target:
                q.append((nx, ny))
                visit[nx][ny] = 1


n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))


ans_one = 0
ans_two = 0
for i in range(2):
    visit = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if visit[x][y] == 0:
                if i == 0:
                    bfs(x, y, graph[x][y])
                    ans_one += 1
                else:
                    bfs_rb(x, y, graph[x][y])
                    ans_two += 1
print(ans_one, ans_two)