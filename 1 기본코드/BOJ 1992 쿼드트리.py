import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]
ret = []

def quadtree(x, y, n):
    if n == 1:
        return str(graph[x][y])

    result = []
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[x][y] != graph[i][j]:
                part = n // 2
                result.append('(')
                result.extend(quadtree(x, y, part))
                result.extend(quadtree(x, y + part, part))
                result.extend(quadtree(x + part, y, part))
                result.extend(quadtree(x + part, y + part, part))
                result.append(')')

                return result
    return str(graph[x][y])

ret.extend(quadtree(0, 0, n))
print("".join(ret))