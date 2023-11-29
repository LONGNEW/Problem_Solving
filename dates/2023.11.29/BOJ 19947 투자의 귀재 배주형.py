import sys

h, y = map(int, sys.stdin.readline().split())
dp = [-float("inf")] * (y + 1)
dp[0] = h

for i in range(y + 1):
    if i + 1 < y + 1:
        dp[i + 1] = max(dp[i + 1], int(dp[i] + dp[i] * 0.05))

    if i + 3 < y + 1:
        dp[i + 3] = max(dp[i + 3], int(dp[i] + dp[i] * 0.2))

    if i + 5 < y + 1:
        dp[i + 5] = max(dp[i + 5], int(dp[i] + dp[i] * 0.35))

print(dp[-1])