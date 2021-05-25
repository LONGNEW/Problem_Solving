import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

data.sort()

for idx, item in enumerate(compare):
    left_idx = bisect_left(data, item)
    right_idx = bisect_right(data, item)
    compare[idx] = right_idx - left_idx

for item in compare:
    print(item, end=" ")
