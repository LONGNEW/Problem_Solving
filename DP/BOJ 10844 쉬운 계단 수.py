import sys

T = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(101)]

for i in range(10):
    dp[1][i] = 1

for x in range(2, 101):
    for y in range(10):
        up = y + 1
        down = y - 1
        if down >= 0:
            dp[x][down] += dp[x - 1][y]
        if up < 10:
            dp[x][up] += dp[x - 1][y]

res = 0
for i in range(10):
    res += dp[T][i]

print((res - dp[T][0]) % 1000000000)