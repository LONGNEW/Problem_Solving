import sys


def dfs(x, y):
    if x == n - 1 and y == n - 1:
        return 1

    if visit[x][y] == -1:
        visit[x][y] = 0
        mv = data[x][y]

        for dx, dy in [(mv, 0), (0, mv)]:
            nx = x + dx
            ny = y + dy

            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue

            visit[x][y] += dfs(nx, ny)

    return visit[x][y]


n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

visit = [[-1] * n for i in range(n)]
dfs(0, 0)

print(visit[0][0])