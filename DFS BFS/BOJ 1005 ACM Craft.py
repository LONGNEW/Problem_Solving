import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, k = map(int, sys.stdin.readline().split())
    data = [0] + list(map(int, sys.stdin.readline().split()))
    degree = [0] * (n + 1)
    graph = [[] for j in range(n + 1)]
    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        degree[y] += 1
        graph[x].append(y)
    target = int(sys.stdin.readline())

    dp = [0] * (n + 1)
    q = []
    for j in range(1, n + 1):
        if degree[j] == 0:
            q.append(j)
            dp[j] = data[j]

    while q:
        now = q.pop(0)

        for next_node in graph[now]:
            degree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[now] + data[next_node])
            if degree[next_node] == 0:
                q.append(next_node)


    print(dp[target])