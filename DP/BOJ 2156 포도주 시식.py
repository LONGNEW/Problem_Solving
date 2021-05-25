import sys

n = int(sys.stdin.readline())
grape = [0]
dp = [0]

for i in range(n):
    data = int(sys.stdin.readline())
    grape.append(data)

dp.append(grape[1])
if n > 1:
    dp.append(grape[1] + grape[2])

for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 2] + grape[i], dp[i - 3] + grape[i] + grape[i - 1]))

print(dp[n])