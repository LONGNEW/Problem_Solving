import sys

dp = [0 for i in range(101)]
dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5] = 2, 2

for i in range(6, 101):
    dp[i] = dp[i - 5] + dp[i - 1]

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])