import sys

def change(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if a[i][j] == '1':
                a[i][j] = '0'
            else:
                a[i][j] = '1'

n, m = map(int, sys.stdin.readline().split())
a, b, cnt = [list(sys.stdin.readline().rstrip()) for _ in range(n)], [list(sys.stdin.readline().rstrip()) for _ in range(n)], 0

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            change(i, j)
            cnt += 1

print(cnt if a == b else -1)