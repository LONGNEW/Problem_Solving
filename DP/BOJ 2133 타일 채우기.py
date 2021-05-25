import sys

N = int(sys.stdin.readline())
dp = [0 for i in range(31)]
dp[2] = 3

for i in range(4, N + 1, 2):
    dp[i] = dp[i - 2] * 3
    for j in range(i - 4, -1, -2):
        dp[i] += dp[j] * 2
    dp[i] += 2


print(dp[N])