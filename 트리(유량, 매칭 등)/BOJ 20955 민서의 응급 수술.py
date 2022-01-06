import sys
from sys import setrecursionlimit
setrecursionlimit(100000)

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a > parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a

n, m = map(int, sys.stdin.readline().split())
parent, cycle = [i for i in range(n + 1)], 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    if find(u) == find(v):
        cycle += 1
    else:
        union(u, v)

edge = 0
for i in range(1, n):
    if find(i) == find(i + 1):
        continue
    union(i, i + 1)
    edge += 1

print(cycle + edge)