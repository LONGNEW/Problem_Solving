import sys
from heapq import heappop, heappush

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 1
while True:
    n = int(sys.stdin.readline())
    data = []
    visit = [[float('inf')] * n for _ in range(n)]

    if n == 0:
        break

    for _ in range(n):
        data.append(list(map(int, sys.stdin.readline().split())))

    temp = []
    visit[0][0] = data[0][0]
    heappush(temp, (data[0][0], 0, 0))

    while temp:
        wei, x, y = heappop(temp)
        if x == n - 1 and y == n - 1:
            break

        if wei > visit[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            next_wei = data[nx][ny]
            if wei + next_wei < visit[nx][ny]:
                heappush(temp, (next_wei + wei, nx, ny))
                visit[nx][ny] = wei + next_wei
    print(f"Problem {cnt}: {visit[n - 1][n - 1]}")
    cnt += 1