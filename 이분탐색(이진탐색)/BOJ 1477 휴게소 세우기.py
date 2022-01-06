import sys

n, m, l = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.append(0)
data.append(l)

data.sort()
left, right = 0, l
while left <= right:
    mid = (left + right) // 2
    if not mid:
        left = mid + 1
        continue
    cnt = 0

    for i in range(1, len(data)):
        cnt += (data[i] - data[i - 1] - 1) // mid

    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)