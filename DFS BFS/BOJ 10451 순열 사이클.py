import sys
sys.setrecursionlimit(10000)

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())

    graph = [0]
    data = list(map(int, sys.stdin.readline().split()))
    for item in data:
        graph.append(item)

    root = [i for i in range(n + 1)]
    visit = [False] * (n + 1)
    cnt = 0

    def DFS(start):
        global cnt
        visit[start] = True

        next_node = graph[start]
        if root[start] == root[next_node]:
            cnt += 1
        else:
            root[next_node] = root[start]
            DFS(next_node)

    for i in range(1, n + 1):
        if not visit[i]:
            DFS(i)
    print(cnt)