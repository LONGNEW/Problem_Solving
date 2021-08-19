import sys


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(one, two):
    parent_one = find(one)
    parent_two = find(two)

    if parent_one < parent_two:
        parent[parent_two] = parent_one
    else:
        parent[parent_one] = parent_two


n, m = map(int, sys.stdin.readline().split())
edge, parent, ans = [], [i for i in range(n + 1)], []

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edge.append((c, a, b))

edge.sort()
idx = 0
while len(ans) < n - 2:
    cost, node_a, node_b = edge[idx]

    if find(node_a) != find(node_b):
        union(node_a, node_b)
        ans.append(cost)

    idx += 1

print(sum(ans))