import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

low = 1
high = max(data)

while low <= high:
    mid = (low + high) // 2
    dis = 0
    for item in data:
        if item - mid > 0:
            dis += item - mid
    if dis >= m:
        low = mid + 1
    else:
        high = mid - 1

print(high)