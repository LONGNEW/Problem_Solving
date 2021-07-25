import sys

T = int(sys.stdin.readline())
result = []

for i in range(T):
    n = int(sys.stdin.readline())
    score = []
    dp = [[0] * n for _ in range(2)]

    for j in range(2):
        data = list(map(int, sys.stdin.readline().split()))
        score.append(data)

    if n == 1:
        print(max(max(score[0]), max(score[1])))
        continue

    dp[0][0] = score[0][0]
    dp[1][0] = score[1][0]

    dp[0][1] = score[0][1] + dp[1][0]
    dp[1][1] = score[1][1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + score[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + score[1][i]

    result.append(max(dp[0][n - 1], dp[1][n - 1]))

for i in result:
    print(i)