import sys
sys.setrecursionlimit(100000)

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
parent = [i for i in range(n + 1)]
for i in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c == 0:
        if find(a) != find(b):
            union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")