import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

limit = sum(cost) + 1
dp = [[0] * limit for i in range(n + 1)]

ans = 999999999

for i in range(1, n + 1):
    now_data, now_cost = data[i - 1], cost[i - 1]

    for j in range(limit):
        if j >= now_cost:
            dp[i][j] = max(now_data + dp[i - 1][j - now_cost], dp[i - 1][j])

            if dp[i][j] >= m:
                ans = min(ans, j)
        else:
            dp[i][j] = dp[i - 1][j]
print(ans)