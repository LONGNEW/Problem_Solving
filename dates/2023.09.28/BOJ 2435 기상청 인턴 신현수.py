import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

ret = -float("inf")
for i in range(n - k + 1):
    temp = 0

    for j in range(i, i + k):
        temp += data[j]

    ret = max(ret, temp)
print(ret)