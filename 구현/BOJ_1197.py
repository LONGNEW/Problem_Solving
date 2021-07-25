import sys

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v + 1)]
edge = []

for i in range(e):
    edge.append(tuple(map(int, sys.stdin.readline().split())))

edge.sort(key=lambda x:x[2])
ans = 0

for a, b, c in edge:
    if find(a) != find(b):
        union(a, b)
        ans += c

print(ans)