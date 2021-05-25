import sys
from heapq import heappop, heappush
from collections import deque


def bfs():
    fish = []
    q = deque([(baby_x, baby_y, 0)])
    visit = [[0] * n for i in range(n)]
    visit[baby_x][baby_y] = 1
    cnt = 0

    while q:
        x, y, dis = q.popleft()

        if cnt != dis:
            if len(fish) != 0:
                return fish
            cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny] == 0 and graph[nx][ny] <= baby_size:
                q.append((nx, ny, dis + 1))
                visit[nx][ny] = 1

                if graph[nx][ny] < baby_size and graph[nx][ny] != 0:
                    heappush(fish, (dis + 1, nx, ny))
    return fish


n = int(sys.stdin.readline())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

baby_x, baby_y = 0, 0
baby_size = 2

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if temp[j] == 9:
            baby_x, baby_y = i, j
            temp[j] = 0
    graph.append(temp)

ans = 0
cnt = 0
while True:
    a = bfs()
    cnt += 1
    if len(a) == 0:
        break

    dis, x, y = heappop(a)
    baby_x, baby_y = x, y
    if cnt == baby_size:
        cnt = 0
        baby_size += 1

    graph[x][y] = 0
    ans += dis

print(ans)

