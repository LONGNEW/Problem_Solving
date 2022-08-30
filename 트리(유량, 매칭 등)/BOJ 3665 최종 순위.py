import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    prev = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    degree = [0] * (n + 1)

    for i in range(n - 1, 0, -1):
        node = prev[i]
        degree[node] = i

    now_degree = [i for i in degree]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if degree[a] > degree[b]:
            now_degree[a] -= 1
            now_degree[b] += 1
        else:
            now_degree[b] -= 1
            now_degree[a] += 1

    temp = []
    for node in range(1, n + 1):
        deg = now_degree[node]
        temp.append((deg, node))

    temp.sort()
    flag = 0
    for i in range(n - 1):
        if flag:
            continue

        deg1, deg2 = temp[i][0], temp[i + 1][0]
        if deg1 == deg2:
            flag = 1

    if flag:
        print("IMPOSSIBLE")
        continue

    for deg, node in temp:
        print(node, end=" ")
    print()
