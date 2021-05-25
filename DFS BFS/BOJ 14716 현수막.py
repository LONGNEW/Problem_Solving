import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def dfs(x, y):
    graph[x][y] = 0
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(len(dy)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny]:
            dfs(nx, ny)

for i in range(N):
    for j in range(M):
        if graph[i][j]:
            dfs(i, j)
            ans += 1
print(ans)