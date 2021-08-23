import sys

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
n, l, r = map(int, sys.stdin.readline().split())
data = []

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

day = 0
while True:
    visit = [[0] * n for i in range(n)]
    value = [0]
    cnt = 1

    for x in range(n):
        for y in range(n):
            if visit[x][y] != 0:
                continue

            temp_value, temp_cnt, visit[x][y] = data[x][y], 1, cnt
            temp = [(x, y)]
            while temp:
                now_x, now_y = temp.pop()

                for i in range(4):
                    nx = now_x + dx[i]
                    ny = now_y + dy[i]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if visit[nx][ny] == 0 and l <= abs(data[now_x][now_y] - data[nx][ny]) <= r:
                        visit[nx][ny] = cnt
                        temp_cnt += 1
                        temp_value += data[nx][ny]
                        temp.append((nx, ny))

            if temp_cnt > 1:
                value.append(temp_value // temp_cnt)
                cnt += 1
            else:
                visit[x][y] = 0

    if cnt == 1:
        break

    for x in range(n):
        for y in range(n):
            if visit[x][y] == 0:
                continue

            data[x][y] = value[visit[x][y]]

    day += 1

print(day)