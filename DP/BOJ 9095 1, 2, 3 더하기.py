import sys

T = int(sys.stdin.readline())
data = []
for i in range(T):
    num = int(sys.stdin.readline().strip())
    data.append(num)

dp = [0, 1, 2, 4]

for i in range(4, 11):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

for i in data:
    print(dp[i])