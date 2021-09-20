import sys

n = int(sys.stdin.readline())
data = [[' '] * n for _ in range(n)]

idx = n - 1
for i in range(n):
    data[0][i] = '*'
    data[-1][i] = '*'
    data[i][i] = '*'
    data[idx][i] = '*'
    data[i][0] = '*'
    data[i][-1] = '*'
    idx -= 1

for i in range(n):
    for j in range(n):
        print(data[i][j], end="")
    print()