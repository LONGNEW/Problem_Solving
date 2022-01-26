import sys

n, m = map(int, sys.stdin.readline().split())
boy = list(map(int, sys.stdin.readline().split()))
girl = list(map(int, sys.stdin.readline().split()))
ans = [[float("inf")] * (m + 1) for _ in range(n + 1)]

boy.sort()
girl.sort()

for i in range(n + 1):
    ans[i][0] = 0
for i in range(m + 1):
    ans[0][i] = 0

for x in range(1, n + 1):
    for y in range(1, m + 1):

        if x == y:
            ans[x][y] = ans[x - 1][y - 1] + abs(boy[x - 1] - girl[y - 1])
        elif x > y:
            ans[x][y] = min(ans[x - 1][y], ans[x - 1][y - 1] + abs(boy[x - 1] - girl[y - 1]))
        else:
            ans[x][y] = min(ans[x][y - 1], ans[x - 1][y - 1] + abs(boy[x - 1] - girl[y - 1]))

print(ans[n][m])