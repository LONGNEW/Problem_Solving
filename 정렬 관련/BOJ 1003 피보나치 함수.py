import sys

data = [[0] * 41 for i in range(2)]

data[0][0] = 1
data[1][0] = 0

data[0][1] = 0
data[1][1] = 1

data[0][2] = 1
data[1][2] = 1

for i in range(3, 41):
    data[0][i] = data[0][i - 1] + data[0][i - 2]
    data[1][i] = data[1][i - 1] + data[1][i - 2]

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    print(data[0][n], data[1][n])