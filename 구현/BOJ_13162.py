import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

diff = data[-1] - data[0]
idxs = []
for i in range(1, len(data)):
    idxs.append(data[i] - data[i - 1])

idxs.sort(key=lambda x:-x)
for idx in range(1, k):
    diff -= idxs[idx - 1]

print(diff)