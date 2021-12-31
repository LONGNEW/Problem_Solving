import sys

n, m = map(int, sys.stdin.readline().split())
graph, dp = [], [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)

for x in range(1, n + 1):
    for y in range(1, m + 1):
        dp[x][y] = dp[x - 1][y] + dp[x][y - 1] - dp[x - 1][y - 1] + graph[x - 1][y - 1]

k = int(sys.stdin.readline())
for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])
    