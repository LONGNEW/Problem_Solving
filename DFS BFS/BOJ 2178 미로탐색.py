import sys
from _collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n)]

for i in range(n):
    data = sys.stdin.readline().strip()
    for item in data:
        graph[i].append(int(item))

def BFS():
    q = deque([(0, 0, 0)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        now_x, now_y, move = q.popleft()
        if now_x == n - 1 and now_y == m - 1:
            return move + 1
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if graph[nx][ny]:
                graph[nx][ny] = 0
                q.append((nx, ny, move + 1))
print(BFS())