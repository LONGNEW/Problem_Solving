import sys

def direction_change(to):
    global idx
    idx += to
    idx %= 4


n = int(sys.stdin.readline())
graph, direction = [[0] * n for _ in range(n)], []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1

for i in range(int(sys.stdin.readline())):
    a, b = sys.stdin.readline().split()
    direction.append((int(a), b))

direction.sort(key=lambda x:-x[0])
x, y, idx, day = 0, 0, 0, 0
body = [(x, y)]

while x >= 0 and x < n and y >= 0 and y < n and graph[x][y] != 2:
    if direction and day == direction[-1][0]:
        temp = direction.pop()
        if temp[1] == 'D':
            direction_change(1)
        else:
            direction_change(-1)

    if graph[x][y] == 0:
        head = body.pop(0)
        graph[head[0]][head[1]] = 0

    if graph[x][y] != 2:
        body.append((x, y))
        graph[x][y] = 2

    x += dx[idx]
    y += dy[idx]

    day += 1

print(day)
