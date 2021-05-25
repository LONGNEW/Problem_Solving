import sys

X, Y = map(int, sys.stdin.readline().split())
pivot = int(Y * 100 / X)

start = 0
end = 1000000000
while start <= end:
    mid = (start + end) // 2
    compare = int((Y + mid) * 100 / (X + mid))
    if compare > pivot:
        end = mid - 1
    else:
        start = mid + 1
if pivot >= 99:
    print(-1)
else:
    print(start)