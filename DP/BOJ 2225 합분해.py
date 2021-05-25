import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[1] * 201 for i in range(201)]

for i in range(1, 201):
    for j in range(2, 201):
        data = 0
        for l in range(i, -1, -1):
            data += dp[l][j - 1]
        dp[i][j] = data


print(dp[n][k] % 1000000000)
