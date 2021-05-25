import sys

N = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split()))
max_pivot = int(sys.stdin.readline())

low = 0
high = max(money)

while low <= high:
    mid = (low + high) // 2
    sum = 0
    for i in money:
        if i > mid:
            sum += mid
        else:   sum += i
    if sum > max_pivot: high = mid - 1
    else:   low = mid + 1
print(high)