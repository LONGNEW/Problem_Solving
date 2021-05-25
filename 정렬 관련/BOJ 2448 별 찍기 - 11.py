import sys

n = int(sys.stdin.readline())
graph = [[" "] * (2 * n - 1) for i in range(n)]

def star(x, y, n):
    if n == 3:
        graph[x][y] = '*'
        graph[x + 1][y - 1] = '*'
        graph[x + 1][y + 1] = '*'
        graph[x + 2][y - 2] = '*'
        graph[x + 2][y - 1] = '*'
        graph[x + 2][y] = '*'
        graph[x + 2][y + 1] = '*'
        graph[x + 2][y + 2] = '*'
    else:
        star(x + n // 2, y - n // 2, n // 2)
        star(x + n // 2, y + n // 2, n // 2)
        star(x, y, n // 2)

star(0, n - 1, n)
for i in range(len(graph)):
        print("".join(graph[i]))
