import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[1] = 0
        continue
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])