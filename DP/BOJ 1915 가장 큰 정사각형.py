import sys

n, m = map(int, sys.stdin.readline().split())
data = [[0] * (m + 1)]
for i in range(n):
    data.append([0] + list(map(int, sys.stdin.readline().rstrip())))

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if data[i][j] == 1:
            data[i][j] += min(data[i - 1][j], data[i - 1][j - 1], data[i][j - 1])
        ans = max(ans, data[i][j])

print(ans ** 2)