import sys

n = int(sys.stdin.readline())
graph = []
top = 0
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

temp = n
while temp > 1:
    temp //= 3
    top += 1

def check(x, y, target, move):
    for i in range(x, x + move):
        for j in range(y, y + move):
            if graph[i][j] != target:
                return False
    return True

def twos(x, y, move):
    for i in range(x, x + move):
        for j in range(y, y + move):
            graph[i][j] = 2


zeros = 0
ones = 0
minuses = 0

while top >= 0:
    move = 3 ** top
    for x in range(0, n, move):
        for y in range(0, n, move):
            if graph[x][y] == 2:
                continue
            if check(x, y, graph[x][y], move):
                if graph[x][y] == 0:
                    zeros += 1
                elif graph[x][y] == 1:
                    ones += 1
                else:
                    minuses += 1
                twos(x, y, move)
    top -= 1
print(minuses)
print(zeros)
print(ones)