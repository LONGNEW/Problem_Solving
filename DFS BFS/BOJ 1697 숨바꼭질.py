import sys
from _collections import deque

n, k = map(int, sys.stdin.readline().split())
dp = [0 for i in range(100001)]

q = deque([])
q.append((n, 1))

while q:
    now, cnt = q.popleft()
    dp[now] = cnt

    if now == k:
        break

    if now - 1 >= 0 and dp[now - 1] == 0:
        dp[now - 1] = cnt + 1
        q.append((now - 1, cnt + 1))
    if now * 2 <= 100000 and dp[now * 2] == 0:
        dp[now * 2] = cnt + 1
        q.append((now * 2, cnt + 1))
    if now + 1 <= 100000 and dp[now + 1] == 0:
        dp[now + 1] = cnt + 1
        q.append((now + 1, cnt + 1))

print(dp[k] - 1)