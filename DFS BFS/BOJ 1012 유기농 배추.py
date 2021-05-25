import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())
ans = []

def DFS(navi, position):
    navi[position[0]][position[1]] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(len(dx)):
        nx = position[0] + dx[i]
        ny = position[1] + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if navi[nx][ny]:
            DFS(navi, [nx, ny])

for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]

    for i in range(k):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    cnt = 0

    for x in range(n):
        for y in range(m):
            if graph[x][y]:
                DFS(graph, [x, y])
                cnt += 1

    ans.append(cnt)

for data in ans:
    print(data)