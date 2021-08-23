import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
data, pos = [], []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    data.append(temp)

    for j in range(n):
        if temp[j] != 0:
            pos.append((temp[j], i, j))

s, x, y = map(int, sys.stdin.readline().split())
pos.sort()
q = deque(pos)

for i in range(s):

    for j in range(len(q)):
        value, now_x, now_y = q.popleft()

        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if data[nx][ny] == 0:
                data[nx][ny] = data[now_x][now_y]
                q.append((data[now_x][now_y], nx, ny))

print(data[x - 1][y - 1])