import sys

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())

data = [[0] * (len(a) + 1) for i in range(len(b) + 1)]

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        b_idx = i - 1
        a_idx = j - 1
        if a[a_idx] == b[b_idx]:
            data[i][j] = data[i - 1][j - 1] + 1
        else:
            data[i][j] = max(data[i - 1][j], data[i][j - 1])

print(data[-1][-1])