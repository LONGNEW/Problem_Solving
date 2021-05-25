import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
left = defaultdict(int)
ans = 0


def dfs(idx, end_idx, subtotal, direction):
    global ans
    if idx == end_idx:
        if direction == 'right':
            ans += left[s - subtotal]
        else:
            left[subtotal] += 1
        return

    dfs(idx + 1, end_idx, subtotal, direction)
    dfs(idx + 1, end_idx, subtotal + data[idx], direction)


dfs(0, n // 2, 0, 'left')
dfs(n // 2, n, 0, 'right')

if s != 0:
    print(ans)
else:
    print(ans - 1)