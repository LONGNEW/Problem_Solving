import sys
from heapq import heappop, heappush


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)
    if  root_y > root_x:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edge = []
parent = [i for i in range(n + 1)]
ans = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    heappush(edge, (c, a, b))

for i in range(m):
    cost, a, b = heappop(edge)

    if find_parent(a) != find_parent(b):
        union(a, b)
        ans += cost
print(ans)