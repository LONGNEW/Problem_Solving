import sys

n, m = map(int, sys.stdin.readline().split())
data = [[0] * (m + 1) for i in range(n + 1)]
s = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    a = list(map(int, sys.stdin.readline().strip()))
    for j in range(1, len(a) + 1):
        data[i][j] = a[j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + data[i][j]


def add(x, y, nx, ny):
    return s[nx][ny] - s[nx][y - 1] - s[x - 1][ny] + s[x - 1][y - 1]


ans = 0
# 직사각형의 모양이 세로로 3가지 일 때.
# 세로 길이는 n으로 고정이고. 가로길이를 3등분 해야 하기 때문에
# 1 ~ i, i + 1 ~ j, j + 1 ~ m
for i in range(1, m - 1):
    for j in range(i + 1, m):
        r1 = add(1, 1, n, i)
        r2 = add(1, i + 1, n, j)
        r3 = add(1, j + 1, n, m)
        ans = max(ans, r1 * r2 * r3)

# 직사각형의 모양이 가로로 3가지 일 때.
# 가로 길이는 m으로 고정이고. 세로길이를 3등분 해야 하기 때문에
# 1 ~ i, i + 1 ~ j, j + 1 ~ n
for i in range(1, n - 1):
    for j in range(i + 1, n):
        r1 = add(1, 1, i, m)
        r2 = add(i + 1, 1, j, m)
        r3 = add(j + 1, 1, n, m)
        ans = max(ans, r1 * r2 * r3)

for i in range(1, n):
    for j in range(1, m):
        # 세로로 n을 가지는 모양
        r1 = add(1, 1, n, j)
        # 가로 모양 중 위에 꺼.
        # 1, j + 1 에 위치 위의 세로 모양이 n, j 까지의 넓이를 가지기 때문.
        r2 = add(1, j + 1, i, m)
        r3 = add(i + 1, j + 1, n, m)
        ans = max(ans, r1 * r2 * r3)

        r1 = add(1, 1, i, j)
        r2 = add(i + 1, 1, n, j)
        r3 = add(1, j + 1, n, m)
        ans = max(ans, r1 * r2 * r3)

        r1 = add(1, 1, i, m)
        r2 = add(i + 1, 1, n, j)
        r3 = add(i + 1, j + 1, n, m)
        ans = max(ans, r1 * r2 * r3)

        r1 = add(1, 1, i, j)
        r2 = add(1, j + 1, i, m)
        r3 = add(i + 1, 1, n, m)
        ans = max(ans, r1 * r2 * r3)
print(ans)