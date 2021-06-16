import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
low, high = 0, 0

for item in data:
    high += item

while low <= high:
    mid = (low + high) // 2

    cnt, total = 0, 0

    for i in range(len(data)):
        total += data[i]
        if total >= mid:
            cnt += 1
            total = 0

    if cnt >= k:
        low = mid + 1
    else:
        high = mid - 1

print(high)