import sys

n = int(sys.stdin.readline())
ord_edge = []
edges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    ord_edge.append((a, b))
    edges[a].append(b)
    edges[b].append(a)

q = int(sys.stdin.readline())
for _ in range(q):
    t, k = map(int, sys.stdin.readline().split())

    if t == 1:
        print("no" if len(edges[k]) == 1 else "yes")
    else:
        n1, n2 = ord_edge[k - 1]
        print("yes")