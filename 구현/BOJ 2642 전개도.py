import sys


def dfs(x, y, direction, now_direct, cnt, num):
    if cnt == 2 and direction == now_direct:
        oppo[num].append(graph[x][y])
        return

    visit[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 6 or ny < 0 or ny >= 6:
            continue
        if graph[nx][ny] == 0:
            continue
        if visit[nx][ny] == 1:
            continue

        if direction == i:
            cnt += 1
        visit[nx][ny] = 1
        dfs(nx, ny, direction, i, cnt, num)

        if direction == i:
            cnt -= 1

    return 0


graph, oppo = [], [[] for _ in range(7)]

# 오른쪽, 왼쪽, 아래, 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(6):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)

total = 0
for item in graph:
    total += sum(item)

if total != 21:
    print(0)
    exit(0)

for x in range(6):
    for y in range(6):

        if graph[x][y] != 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= 6 or ny < 0 or ny >= 6:
                    continue
                if graph[nx][ny] == 0:
                    continue

                visit = [[0] * 6 for _ in range(6)]
                visit[x][y] = 1
                dfs(nx, ny, i, i, 1, graph[x][y])

flag = 0
for item in oppo[1:]:
    if len(item) >= 2 or len(item) == 0:
        flag = 1

if not flag:
    print(oppo[1][0])
else:
    print(0)