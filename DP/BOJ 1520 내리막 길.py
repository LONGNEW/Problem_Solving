import sys


def dfs(x, y):

    if x == 0 and y == 0:
        return 1
    # 방문을 하지 않은 점에 대해서 dfs를 수행한다.
    if visit[x][y] == -1:
        visit[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= h or nx < 0 or ny >= w or ny < 0:
                continue
            # 처음부터 내가 찾으려 한 값은 [h][w]에 올 수 있는 모든 경로를
            # 기록한 후에 이를 더해서 찾으려 하였다.
            # 그렇다면 이것을 어떻게 해야 하는가 가능 한 경로들을 각 위치에 저장
            # 하도록 해 주는 것이 바람직하다.
            # 그렇기 때문에 각 위치 x, y 에서 nx, ny로 이동을 할 수 있다면
            # 그 위치까지 올 수 있는 경로를 다 더해 주기 위해
            # 아래 에서 처럼 dfs를 수행하고 이를 visit에 저장하는 것이다.

            if data[nx][ny] > data[x][y]:
                visit[x][y] += dfs(nx, ny)

    # 이미 방문을 한 지점이라면 그냥 return 해준다.
    return visit[x][y]


h, w = map(int, sys.stdin.readline().split())
data = []
for i in range(h):
    temp = list(map(int, sys.stdin.readline().split()))
    data.append(temp)

visit = [[-1] * w for i in range(h)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

print(dfs(h - 1, w - 1))