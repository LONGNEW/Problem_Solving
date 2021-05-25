import sys

data = list(sys.stdin.readline().strip())
dp = [[1] * len(data) for i in range(2)]

if data[0] == '0':
    print(0)
else:
    dp[1][0] = 0
    for i in range(1, len(data)):
        if not (10 <= int(data[i - 1] + data[i]) <= 26):
            dp[0][i] = 0
        if not (1 <= int(data[i]) <= 10):
            dp[1][i] = 0

    for i in range(2, len(data)):
        if dp[0][i]:
            dp[0][i] = dp[0][i - 2] + dp[1][i - 2]
        if dp[1][i]:
            dp[1][i] = dp[0][i - 1] + dp[1][i - 1]

    print((dp[0][len(data) - 1] + dp[1][len(data) - 1]) % 1000000)