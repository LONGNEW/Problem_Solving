import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edge = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a - 1][b - 1] = min(edge[a - 1][b - 1], c)

for i in range(n):
    edge[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

for i in range(n):
    for j in range(n):
        if edge[i][j] == float('inf'):
            edge[i][j] = 0

for i in range(n):
    print(*edge[i])