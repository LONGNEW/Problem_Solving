def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

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

edges = []
results = 0

for i in range(edge_num):
    A, B, cost = map(int, input().split())
    edges.append((cost, A, B))

edges.sort()

for item in edges:
    cost, a, b = item
    if find_parent(parent, a) != find_parent(parent, b):
        results += cost
        union(parent, a, b)

print(results)