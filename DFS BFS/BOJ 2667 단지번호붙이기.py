import sys
from _collections import deque

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))
group = []

def BFS(x, y):
    q = deque([(x, y)])
    graph[x][y] = '0'
    cnt = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        now_x, now_y = q.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or nx >= n or ny >= n or ny < 0:
                continue
            if graph[nx][ny] == '1':
                graph[nx][ny] = '0'
                cnt += 1
                q.append((nx, ny))
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            group.append(BFS(i, j))
print(len(group))
group.sort()
for item in group:
    print(item)