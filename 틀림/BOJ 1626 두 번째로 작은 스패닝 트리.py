import sys
from heapq import heappop, heappush

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

def dfs(node, deep):
    depth[node] = deep

    for next_node, cost in graph[node]:
        if depth[next_node] == -1:
            prev[next_node][0] = node
            first[next_node][0] = cost
            dfs(next_node, deep + 1)

def set_prev():
    dfs(1, 0)

    for log in range(1, 22):
        for node in range(1, v + 1):
            if prev[node][log - 1] == 0:
                continue
            prev[node][log] = prev[prev[node][log - 1]][log - 1]

            if prev[node][log] == 0:
                continue

            if first[node][log - 1] > first[prev[node][log - 1]][log - 1]:
                first[node][log] = first[node][log - 1]
                second[node][log] = first[prev[node][log - 1]][log - 1]
            else:
                second[node][log] = first[node][log - 1]
                first[node][log] = first[prev[node][log - 1]][log - 1]
def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for log in range(20, -1, -1):
        if depth[b] - depth[a] >= (1 << log):
            b = prev[b][log]

    if a == b:
        return a

    for log in range(20, -1, -1):
        if prev[b][log] != prev[a][log]:
            b = prev[b][log]
            a = prev[a][log]

    return prev[a][0]

def get_distance(node, root):
    for log in range(20, -1, -1):
        if depth[node] - depth[root] >= (1 << log):

            if first[node][log] != float('inf'):
                heappush(edges, -first[node][log])
                if len(edges) == 3:
                    heappop(edges)

            if second[node][log] != float('inf'):
                heappush(edges, -second[node][log])
                if len(edges) == 3:
                    heappop(edges)

            node = prev[node][log]

v, e = map(int, sys.stdin.readline().split())
edge, parent, remain, graph = [], [i for i in range(v + 1)], [], dict()

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    heappush(edge, (c, a, b))

for i in range(1, v + 1):
    graph[i] = []

original = 0
while edge:
    c, a, b = heappop(edge)

    if find(a) == find(b):
        remain.append((c, a, b))
        continue

    union(a, b)
    graph[a].append((b, c))
    graph[b].append((a, c))
    original += c

root = parent[1]

# 연결 된 모든 점들의 부모 노드 업데이트
# 중간 지점의 노드가 업데이트 된 경우 이 보다 하위
# 노드에서는 아직 중간 지점을 부모로 생각할 수 있음.
for i in range(2, v + 1):
    if parent[i] != root:
        parent[i] = find(parent[i])

for i in range(2, v + 1):
    if parent[i] != root:
        print(-1)
        exit(0)

depth, prev, ans = [-1] * (v + 1), [[0] * 21 for i in range(v + 1)], float('inf')
first, second = [[float('inf')] * 21 for i in range(v + 1)], [[float('inf')] * 21 for i in range(v + 1)]

set_prev()
for c, a, b in remain:
    edges = []

    sub_root = lca(a, b)

    if a != sub_root:
        get_distance(a, sub_root)

    if b != sub_root:
        get_distance(b, sub_root)

    for i in range(2):
        if len(edges) == 0:
            break

        distance = -heappop(edges)

        if distance != c:
            ans = min(ans, original + c - distance)

if ans == float('inf'):
    print(-1)
    exit(0)

print(ans)