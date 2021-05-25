import sys

k, n = map(int, sys.stdin.readline().split())
data = []

low = 1
high = -999

for i in range(k):
    num = int(sys.stdin.readline())
    data.append(num)
    high = max(high, num)

while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for item in data:
        cnt += item // mid
    if cnt >= n:
        low = mid + 1
    else:
        high = mid - 1

print(high)