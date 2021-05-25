import sys
sys.setrecursionlimit(10000)

w, h = map(int, sys.stdin.readline().split())
ans = []
def DFS(navi, position):

    navi[position[0]][position[1]] = 0

    dx = [1, -1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 1, -1, -1, 1, -1, 1]

    for i in range(len(dx)):
        nx = position[0] + dx[i]
        ny = position[1] + dy[i]
        if nx >= h or nx < 0 or ny >= w or ny < 0:
            continue
        if navi[nx][ny]:
            DFS(navi, [nx, ny])

while w != 0 and h != 0:
    graph = []
    cnt = 0
    for i in range(h):
        data = list(map(int, sys.stdin.readline().split()))
        graph.append(data)

    for x in range(h):
        for y in range(w):
            if graph[x][y]:
                DFS(graph, [x, y])
                cnt += 1

    ans.append(cnt)
    w, h = map(int, sys.stdin.readline().split())

for data in ans:
    print(data)