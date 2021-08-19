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

n = int(sys.stdin.readline())
pos, edge, parent, ans = [[], [], []], [], [i for i in range(n)], []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))

    for j in range(3):
        pos[j].append((temp[j], i))

for i in range(3):
    temp = sorted(pos[i])

    for j in range(1, n):
        a_cost, node_a = temp[j][0], temp[j][1]
        b_cost, node_b = temp[j - 1][0], temp[j - 1][1]

        edge.append((abs(a_cost - b_cost), node_a, node_b))

edge.sort()
idx = 0
while len(ans) < n - 1:
    cost, node_a, node_b = edge[idx]

    if find(node_a) != find(node_b):
        union(node_a, node_b)
        ans.append(cost)

    idx += 1

print(sum(ans))