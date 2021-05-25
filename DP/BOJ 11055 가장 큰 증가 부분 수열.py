import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = []

for i in data:
    dp.append(i)

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))