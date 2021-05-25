import sys

N = int(sys.stdin.readline())
data = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(N):
    S = int(sys.stdin.readline())
    data[i] = S
    
dp[0] = data[0]
dp[1] = data[1] + data[0]
dp[2] = max(data[1] + data[2], data[0] + data[2])

for i in range(3, N):
    dp[i] = max(data[i] + data[i - 1] + dp[i - 3], data[i] + dp[i - 2])

print(dp[N - 1])