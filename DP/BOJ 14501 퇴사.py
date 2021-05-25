import sys

n = int(sys.stdin.readline())
data = [[0] * n for i in range(2)]

for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    data[0][i] = t
    data[1][i] = p

dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    if i + data[0][i] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], data[1][i] + dp[i + data[0][i]])
print(dp[0])
