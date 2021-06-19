import sys

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a < parent_b:
        root[b] = parent_a
    else:
        root[a] = parent_b

def find(c):
    if root[c] != c:
        root[c] = find(root[c])
    return root[c]

n, m = map(int, sys.stdin.readline().split())
root = [i for i in range(n + 1)]
ans = set()
cnt = 0

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if find(u) == find(v):
        cnt += 1
    else:
        union(u, v)

for i in range(1, n + 1):
    ans.add(root[i])
print(len(ans) - 1 + cnt)