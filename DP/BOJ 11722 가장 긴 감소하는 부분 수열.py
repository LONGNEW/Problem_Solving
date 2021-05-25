import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

data.reverse()

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
