import sys
from collections import deque

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
ans = deque([(float('INF'), 0, 0, 0)])

for i in range(n - 2):
    left = i + 1
    right = len(data) - 1

    while left < right:
        temp = data[i] + data[left] + data[right]
        compare, prev_i, prev_left, prev_right = ans.popleft()

        if abs(compare) > abs(temp):
            ans.append((temp, i, left, right))
        else:
            ans.append((compare, prev_i, prev_left, prev_right))

        if temp > 0:
            right -= 1
        else:
            left += 1

val, i, left, right = ans.popleft()
print(f"{data[i]} {data[left]} {data[right]}")