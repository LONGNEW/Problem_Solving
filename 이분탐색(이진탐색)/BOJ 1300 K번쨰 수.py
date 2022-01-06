import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

low, high = 1, n * n
while low <= high:
    mid = (low + high) // 2
    cnt = 0

    for i in range(1, n + 1):
        if mid % i != 0:
            cnt += min(n, mid // i)
        else:
            cnt += min(n, mid // i - 1)

    if cnt + 1 > k:
        high = mid - 1
    else:
        low = mid + 1

print(high)