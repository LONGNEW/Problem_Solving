import sys
from heapq import heappop, heappush

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a > parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a

def dfs(node, depth):
    visit[node] = 1
    level[node] = depth

    for next_node, weight in graph[node]:
        if visit[next_node]:
            continue

        l_parent[next_node][0] = [node, weight]
        dfs(next_node, depth + 1)

def set_parent():
    dfs(1, 0)

    for log in range(1, 21):
        for node in range(1, n + 1):

            next_node, next_weight = l_parent[node][log - 1]
            l_parent[node][log] = [l_parent[next_node][log - 1][0], max(next_weight, l_parent[next_node][log - 1][1])]

def lca(high, low):
    ret = 0
    if level[high] > level[low]:
        high, low = low, high

    for log in range(20, -1, -1):
        if level[low] - level[high] >= (1 << log):
            ret = max(ret, l_parent[low][log][1])
            low = l_parent[low][log][0]

    if high == low:
        return ret

    for log in range(20, -1, -1):
        if l_parent[low][log][0] != l_parent[high][log][0]:
            ret = max(ret, max(l_parent[low][log][1], l_parent[high][log][1]))
            low = l_parent[low][log][0]
            high = l_parent[high][log][0]

    return max(ret, l_parent[low][0][1], l_parent[high][0][1])


n, m = map(int, sys.stdin.readline().split())
edge, data, parent, graph = [], [], [i for i in range(n + 1)], [[] for i in range(n + 1)]
l_parent, visit, level = [[[0, 0] for _ in range(21)] for _ in range(n + 1)], [0] * (n + 1), [0] * (n + 1)
mst = 0

for _ in range(m):
    u, v, w = list(map(int, sys.stdin.readline().split()))

    data.append((u, v, w))
    heappush(edge, (w, u, v))

while edge:
    w, u, v = heappop(edge)

    if find(u) != find(v):
        union(u, v)
        graph[u].append((v, w))
        graph[v].append((u, w))

        mst += w

set_parent()
for u, v, w in data:
    cost = lca(u, v)
    print(mst - cost + w)
