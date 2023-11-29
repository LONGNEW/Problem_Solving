import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
lo, hi = max(data), sum(data)

while lo <= hi:
    mid = (lo + hi) // 2

    summ, cnt = 0, 0
    for item in data:
        if summ + item > mid:
            cnt += 1
            summ = 0
        summ += item
    if summ > 0:
        cnt += 1

    if cnt > m:
        lo = mid + 1
    else:
        hi = mid - 1
print(lo)

