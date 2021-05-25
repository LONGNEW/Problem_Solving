def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x

def union(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a < root_b:
        parent[b] = root_a
    else:
        parent[a] = root_b

node, edge_num = map(int, input().split())
parent = [0] * (node + 1)

for i in range(len(parent)):
    parent[i] = i

cycle = False

for i in range(edge_num):
    A, B = map(int, input().split())
    if find_parent(parent, A) == find_parent(parent, B):
        cycle = True
        break
    else:
        union(parent, A, B)
