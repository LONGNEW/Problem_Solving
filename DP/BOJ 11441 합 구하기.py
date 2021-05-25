import sys

n = int(sys.stdin.readline())
data = [0]

for idx, item in enumerate(list(map(int, sys.stdin.readline().split()))):
    data.append(data[idx] + item)

m = int(sys.stdin.readline())
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(data[b] - data[a - 1])