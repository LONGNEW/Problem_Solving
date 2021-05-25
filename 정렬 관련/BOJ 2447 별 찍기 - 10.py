import sys

n = int(sys.stdin.readline())
graph = [["*"] * n for i in range(n)]

def star(x, y, n):

    for i in range(x + n, x + 2 * n):
        for j in range(y + n, y + 2 * n):
            graph[i][j] = " "
    if n != 1:
        part = n // 3
        star(x, y, part)
        star(x, y + n, part)
        star(x, y + 2 * n, part)
        star(x + n, y, part)
        star(x + n, y + 2 * n, part)
        star(x + 2 * n, y, part)
        star(x + 2 * n, y + n, part)
        star(x + 2 * n, y + 2 * n, part)


star(0, 0, n // 3)