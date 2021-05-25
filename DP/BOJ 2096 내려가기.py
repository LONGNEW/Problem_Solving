import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

dpmax = [data[0][0], data[0][1], data[0][2]]
dpmin = [data[0][0], data[0][1], data[0][2]]

for i in range(1, n):
    dpmax = max(dpmax[0], dpmax[1]) + data[i][0], max(dpmax) + data[i][1], max(dpmax[1], dpmax[2]) + data[i][2]
    dpmin = min(dpmin[0], dpmin[1]) + data[i][0], min(dpmin) + data[i][1], min(dpmin[1], dpmin[2]) + data[i][2]
print(max(dpmax), min(dpmin))