import sys

n, s = map(int, sys.stdin.readline().split())
data = []
dp = [0] * n

for i in range(n):
    h, c = map(int, sys.stdin.readline().split())
    data.append((h, c))

data.sort(key=lambda x:x[0])
dp[0] = data[0][1]

idx = 0
value = 0

for i in range(1, n):
    while data[i][0] - data[idx][0] >= s and idx < i:
        value = max(value, dp[idx])
        idx += 1
    dp[i] = value + data[i][1]

print(max(dp))