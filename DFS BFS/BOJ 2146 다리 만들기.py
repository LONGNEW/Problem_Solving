import sys
from _collections import deque

n = int(sys.stdin.readline())
graph = []

for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y, num):
    q = deque([(x, y)])
    graph[x][y] = num

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = num
                q.append((nx, ny))
            elif graph[nx][ny] == 0 and not (now_x, now_y, 0) in queue:
                queue.append((now_x, now_y, 0))

cnt = 2
queue = deque()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            BFS(i, j, cnt)
            cnt += 1

dis = 99999
while queue:
    done = False
    x, y, cnt = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            queue.append((nx, ny, cnt + 1))

        elif graph[nx][ny] > graph[x][y]:
            dis = min(dis, cnt * 2)

        elif graph[nx][ny] < graph[x][y]:
            dis = min(dis, ((cnt + 1) * 2) - 1)

print(dis)
