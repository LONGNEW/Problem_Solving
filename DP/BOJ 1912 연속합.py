import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
ret = [data[0]]

for i in range(1, n):
    ret.append(max(ret[i - 1] + data[i], data[i]))

print(max(ret))