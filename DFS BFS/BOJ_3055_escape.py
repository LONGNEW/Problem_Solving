import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def water():
    times = len(obstacle)
    for i in range(times):
        x, y = obstacle.popleft()

        for j in range(4):
            next_x = x + dx[j]
            next_y = y + dy[j]

            if next_x < 0 or next_x >= r or next_y < 0 or next_y  >= c:
                continue

            if data[next_x][next_y] == ".":
                data[next_x][next_y] = "*"
                obstacle.append((next_x, next_y))

def bfs():
    times = len(q)

    for i in range(times):
        now_x, now_y = q.popleft()

        for j in range(4):
            next_x = now_x + dx[j]
            next_y = now_y + dy[j]

            if next_x < 0 or next_x >= r or next_y < 0 or next_y >= c:
                continue

            if data[next_x][next_y] == ".":
                data[next_x][next_y] = "S"
                q.append((next_x, next_y))

            if data[next_x][next_y] == "D":
                return 1;
    return 0;

r, c = map(int, sys.stdin.readline().split())
data = []

obstacle = deque()
q = deque()
for i in range(r):
    temp = list(sys.stdin.readline().strip())

    for idx, item in enumerate(temp):
        if item == "S":
            q.append((i, idx))
        elif item == "*":
            obstacle.append((i, idx))

    data.append(temp)

cnt = 0
while q:
    cnt += 1
    water()
    ret = bfs()

    if ret == 1:
        print(cnt)
        exit(0)

print("KAKTUS")
