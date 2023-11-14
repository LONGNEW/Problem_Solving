import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
data = []
visit = []
for i in range(n):
    temp = sys.stdin.readline().strip()
    data.append([item for item in temp])
    visit.append([0 for _ in range(n)])

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
q = []
heappush(q, (0, (0, 0)))

max_break_time = float("inf")
while q:
    break_time, pos = heappop(q)
    x, y = pos

    if break_time >= max_break_time:
        continue

    if x == n - 1 and y == n - 1:
        max_break_time = min(max_break_time, break_time)
        continue

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if visit[nx][ny] == 1:
            continue

        visit[nx][ny] = 1
        heappush(q, (break_time + (1 if data[nx][ny] == "0" else 0), (nx, ny)))

print(max_break_time)