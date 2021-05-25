import sys

T = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1

for x in range(1, 1000):
    for y in range(10):
        for k in range(y, 10):
            dp[x + 1][k] += 1 * dp[x][y]

res = 0
for i in range(10):
    res += dp[T][i]

print(res % 10007)