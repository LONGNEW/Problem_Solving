import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

lo = max(data)
hi = sum(data)
while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0
    full = 0
    for item in data:
        if full + item > mid:
            cnt += 1
            full = 0
        full += item
    if full > 0:
        cnt += 1

    if cnt > m:
        lo = mid + 1
    else:
        hi = mid - 1

print(lo)
