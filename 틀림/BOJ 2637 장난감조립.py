import sys


def dfs(node, cnt):
    if len(graph[node]) == 0:
        ans[node] += cnt
        return

    for next_node, next_cnt in graph[node]:
        dfs(next_node, cnt * next_cnt)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
ans = [0] * (n + 1)

for i in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[x].append((y, k))

dfs(n, 1)

for idx, item in enumerate(ans):
    if item != 0:
        print(idx, item)