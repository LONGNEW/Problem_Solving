import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    data.append(temp)

for i in range(1, n):
    idx = i - 1
    data[i][0] += min(data[idx][1], data[idx][2])
    data[i][1] += min(data[idx][0], data[idx][2])
    data[i][2] += min(data[idx][0], data[idx][1])

print(min(data[n - 1]))