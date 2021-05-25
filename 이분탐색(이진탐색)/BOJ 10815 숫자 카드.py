import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

data.sort()

for idx, item in enumerate(compare):
    done = False
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] > item:
            high = mid - 1
        elif data[mid] < item:
            low = mid + 1
        else:
            compare[idx] = 1
            done = True
            break
    if not done:
        compare[idx] = 0

for item in compare:
    print(item, end=" ")