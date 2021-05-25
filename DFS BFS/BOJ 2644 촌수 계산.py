import sys
sys.setrecursionlimit(10000)

def dfs(now, cnt):
    global ans
    if now == target_two:
        ans = cnt
        return

    for next_node in graph[now]:
        if visit[next_node] == 0:
            visit[next_node] = 1
            dfs(next_node, cnt + 1)

n = int(sys.stdin.readline())
target_one, target_two = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [0] * (n + 1)
ans = -1
dfs(target_one, 0)

print(ans)
