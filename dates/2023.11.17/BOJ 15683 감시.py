import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
cctvs = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

modes = {
    # with dx, dy indexes
    1: [[0], [1], [2], [3]],
    2 : [[0, 1], [2, 3]],
    3 : [[0, 2], [0, 3], [1, 2], [1, 3]],
    4 : [[0, 1, 2], [0, 1, 3], [2, 3, 0], [2, 3, 1]],
    5 : [[0, 1, 2, 3]]
}

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        if temp[j] not in [0, 6]:
            cctvs.append((i, j, temp[j]))
    graph.append(temp)

answer = float("inf")
def dfs(idx):
    global answer, graph
    if idx == len(cctvs):
        cnt = 0
        for row in graph:
            for item in row:
                if item == 0:
                    cnt += 1
        answer = min(answer, cnt)
        return

    x, y, mode = cctvs[idx]
    temp_map = []
    for row in graph:
        temp_row = []
        for item in row:
            temp_row.append(item)
        temp_map.append(temp_row)

    for idxes in modes[mode]:
        for direct in idxes:
            nx, ny = x, y
            while True:
                nx, ny = nx + dx[direct], ny + dy[direct]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break
                if graph[nx][ny] == 6:
                    break

                if graph[nx][ny] == 0:
                    graph[nx][ny] = "#"
        dfs(idx + 1)

        for row in range(len(graph)):
            for col in range(len(graph[0])):
                graph[row][col] = temp_map[row][col]

dfs(0)
print(answer)

