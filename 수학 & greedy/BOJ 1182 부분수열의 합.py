import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(1, n + 1):
    for item in combinations(data, i):
        if sum(item) == s:
            ans += 1
print(ans)
