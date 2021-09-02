import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))
data.sort()

temp = [data[0][1]]
for i in range(1, len(data)):
    if temp[-1] < data[i][1]:
        temp.append(data[i][1])
    else:
        idx = bisect_left(temp, data[i][1])
        temp[idx] = data[i][1]

print(n - len(temp))