import sys

n = int(sys.stdin.readline())
graph, visit = [], [[[0] * 3 for _ in range(n + 1)] for _ in range(n + 1)]
prev = {
    0 : 1, 1 : 2, 2 : 0
}

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)

for x in range(n - 1, -1, -1):
    for y in range(n - 1, -1, -1):

        for i in range(3):
            if i == graph[x][y]:
                visit[x][y][i] = 1 + max(visit[x + 1][y][prev[i]], visit[x][y + 1][prev[i]])
            else:
                visit[x][y][i] = max(visit[x + 1][y][i], visit[x][y + 1][i])


print(visit[0][0][0])