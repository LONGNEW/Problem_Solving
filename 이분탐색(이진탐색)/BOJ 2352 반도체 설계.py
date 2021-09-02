import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
temp = [data[0]]

for i in range(1, n):
    if temp[-1] < data[i]:
        temp.append(data[i])
    else:
        idx = bisect_left(temp, data[i])
        temp[idx] = data[i]

print(len(temp))
