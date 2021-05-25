import sys
from _collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())
dp = [-1] * (f + 1)

q = deque([])
q.append((s, 0))

while q:
    now, button = q.popleft()

    if dp[now] != -1:
        continue

    dp[now] = button

    if now + u <= f and dp[now + u] == -1:
        q.append((now + u, button + 1))
    if now - d > 0 and dp[now - d] == -1:
        q.append((now - d, button + 1))

if dp[g] == -1:
    print('use the stairs')
else:
    print(dp[g])