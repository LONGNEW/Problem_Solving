import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [0]

for item in data:
    dp.append(item)

for i in range(2, n + 1):
    for j in range(1, (i // 2) + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[n])