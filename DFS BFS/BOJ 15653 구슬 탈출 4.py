import sys
from collections import deque

def move (x, y, i):
    # i == direction
    cnt = 0
    while graph[x + dx[i]][y + dy[i]] != "#" and graph[x][y] != "O":
        x += dx[i]
        y += dy[i]
        cnt += 1

    return x, y, cnt

def bfs(rx, ry, bx, by):
    q = deque([])
    q.append((rx, ry, bx, by, 0))

    visit = dict()
    visit[(rx, ry, bx, by)] = 1

    while q:
        rx, ry, bx, by, d = q.popleft()

        for i in range(4):
            temp_rx, temp_ry, temp_rcnt = move(rx, ry, i)
            temp_bx, temp_by, temp_bcnt = move(bx, by, i)

            # 동시에 구멍에 들어갈 수 있는 경우를 찾기 위함.
            if graph[temp_bx][temp_by] == "O":
                continue

            if graph[temp_rx][temp_ry] == "O":
                print(d + 1)
                return

            # 위치가 동일한 경우에.
            # 더 많이 이동한 좌표가 다른 구슬을 무시하고 지나간것이 됨
            if temp_rx == temp_bx and temp_ry == temp_by:
                if temp_rcnt > temp_bcnt:
                    temp_rx, temp_ry = temp_rx - dx[i], temp_ry - dy[i]
                else:
                    temp_bx, temp_by = temp_bx - dx[i], temp_by - dy[i]

            if (temp_rx, temp_ry, temp_bx, temp_by) not in visit:
                visit[(temp_rx, temp_ry, temp_bx, temp_by)] = 1
                q.append((temp_rx, temp_ry, temp_bx, temp_by, d + 1))

    print(-1)


n, m = map(int, sys.stdin.readline().split())
graph, rx, ry, bx, by = [], 0, 0, 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x in range(n):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)

    for y in range(m):
        if temp[y] == "R":
            rx, ry = x, y
        if temp[y] == "B":
            bx, by = x, y

bfs(rx, ry, bx, by)
