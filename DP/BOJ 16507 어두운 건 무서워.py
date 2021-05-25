import sys

r, c, q = map(int, sys.stdin.readline().split())
data = []
for i in range(r):
    temp = list(map(int, sys.stdin.readline().split()))
    data.append(temp)

dp = [[0] * (c + 1) for i in range(r + 1)]
for x in range(r):
    for y in range(c):
        dp[x + 1][y + 1] = dp[x][y + 1] + dp[x + 1][y] - dp[x][y] + data[x][y]

for i in range(q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    temp = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    num = (x2 - x1 + 1) * (y2 - y1 + 1)
    print(temp // num)
