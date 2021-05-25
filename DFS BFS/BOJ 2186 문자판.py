import sys

n, m, k = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

target = list(sys.stdin.readline().strip())
dp = [[[-1] * len(target) for i in range(m)] for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, idx):
    if idx == len(target) - 1:
        dp[x][y][idx] = 1
        return dp[x][y][idx]
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]

    dp[x][y][idx] = 0
    for i in range(4):
        temp_x, temp_y = x, y

        for _ in range(k):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == target[idx + 1]:
                    dp[x][y][idx] += dfs(nx, ny, idx + 1)
            temp_x, temp_y = nx, ny

    return dp[x][y][idx]


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == target[0]:
            cnt += dfs(i, j, 0)
print(cnt)