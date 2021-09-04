import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
temp, idxs = [data[0]], [0] * n
idxs[0] = 1

for i in range(1, n):
    if temp[-1] < data[i]:
        temp.append(data[i])
        idxs[i] = len(temp)
    else:
        idx = bisect_left(temp, data[i])
        temp[idx] = data[i]
        idxs[i] = idx + 1

ans, j = [], len(temp)
for i in range(len(idxs) - 1, -1, -1):
    if idxs[i] == j:
        ans.append(data[i])
        j -= 1

    if j < 1:
        break

print(len(ans))
