import sys

n, m = map(int, sys.stdin.readline().split())
data = dict()
for i in range(m):
    temp = int(sys.stdin.readline())
    data[temp] = 1

dp = [[float('inf')] * 142 for i in range(n + 1)]

dp[1][0] = 0

for i in range(2, n + 1):
    if data.get(i):
        continue
    v = 1
    while v * (v + 1) <= 2 * i:
        dp[i][v] = min(dp[i - v][v - 1], dp[i - v][v], dp[i - v][v + 1]) + 1
        v += 1

ans = min(dp[n])
print(-1 if ans == float('inf') else ans)