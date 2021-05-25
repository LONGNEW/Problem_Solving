import sys
from collections import deque

s = int(sys.stdin.readline())
ans = [[-1] * (s + 1) for i in range(s + 1)]
ans[1][0] = 0

q = deque([(1, 0)])

while q:
    x, y = q.popleft()

    if ans[x][x] == -1:
        ans[x][x] = ans[x][y] + 1
        q.append((x, x))

    if x + y <= s and ans[x + y][y] == -1:
        ans[x + y][y] = ans[x][y] + 1
        q.append((x + y, y))

    if x - 1 >= 0 and ans[x - 1][y] == -1:
        ans[x - 1][y] = ans[x][y] + 1
        q.append((x - 1, y))

ret = float('INF')
for item in ans[s]:
    if item != -1 and ret > item:
        ret = item
print(ret)