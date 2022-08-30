import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    prev = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    degree = [0] * (n + 1)
    graph = [dict() for _ in range(n + 1)]

    for i in range(n - 1, 0, -1):
        node = prev[i]
        degree[node] = i

        for j in range(i - 1, -1, -1):
            next_node = prev[j]
            graph[next_node][node] = 1


    now_degree = [i for i in degree]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if degree[a] > degree[b]:
            del graph[b][a]
            graph[a][b] = 1
            now_degree[a] -= 1
            now_degree[b] += 1
        else:
            del graph[a][b]
            graph[b][a] = 1
            now_degree[b] -= 1
            now_degree[a] += 1

    q = deque([])
    for i in range(1, n + 1):
        if now_degree[i] == 0:
            q.append(i)

    ans = []
    while q and len(q) < 2:
        node = q.popleft()
        ans.append(node)

        for next_node in graph[node].keys():
            now_degree[next_node] -= 1
            if now_degree[next_node] == 0:
                q.append(next_node)

    if len(q) > 1:
        print("?")
    elif len(ans) != n:
        print("IMPOSSIBLE")
    else:
        print(*ans)
