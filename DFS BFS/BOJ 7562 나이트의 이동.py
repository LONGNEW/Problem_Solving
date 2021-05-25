import sys
from _collections import deque

t = int(sys.stdin.readline())
for j in range(t):
    i = int(sys.stdin.readline())
    graph = [[0] * i for k in range(i)]
    start_x, start_y = map(int, sys.stdin.readline().split())
    target_x, target_y = map(int, sys.stdin.readline().split())

    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]

    q = deque([(start_x, start_y, 0)])
    graph[start_x][start_y] = 1
    flag = 0
    ans = 0
    if start_x == target_x and start_y == target_y:
        flag = 1

    if not flag:
        while q:
            now_x, now_y, cnt = q.popleft()
            for k in range(len(dx)):
                nx = now_x + dx[k]
                ny = now_y + dy[k]
                if nx >= i or ny >= i or nx < 0 or ny < 0:
                    continue

                if nx == target_x and ny == target_y:
                    ans = cnt + 1
                    flag = 1
                    break


                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))
            if flag:
                break
    print(ans)



