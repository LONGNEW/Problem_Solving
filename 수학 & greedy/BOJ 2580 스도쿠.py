import sys

graph = []
zeros = []
for i in range(9):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if data[j] == 0:
            zeros.append((i, j))
    graph.append(data)


def possible(x, y):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        if graph[i][y] in num:
            num.remove(graph[i][y])
        if graph[x][i] in num:
            num.remove(graph[x][i])

    start_x = x // 3 * 3
    start_y = y // 3 * 3
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if graph[i][j] in num:
                num.remove(graph[i][j])
    return num


flag = False


def dfs(i):
    global flag

    if flag:
        return

    if i == len(zeros):
        for j in range(9):
            for k in range(9):
                print(graph[j][k], end=" ")
            print()
        flag = True
        return

    else:
        x, y = zeros[i]
        nums = possible(x, y)
        for item in nums:
            graph[x][y] = item
            dfs(i + 1)
            graph[x][y] = 0


dfs(0)