import sys
from _collections import deque

n = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]


for i in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def bfs(start):
    q = deque()
    q.append((start, 0))
    visit[start] = 1
    ret = -9999

    while q:
        now, dis = q.popleft()
        for link in graph[now]:
            next_node, next_dis = link[0], link[1]
            if not visit[next_node]:
                visit[next_node] = 1
                q.append((next_node, dis + next_dis))
        if dis > ret:
            ret = dis
            node = now
    return ret, node


rad = -9999
visit = [0] * (n + 1)
dis, b = bfs(1)

visit = [0] * (n + 1)
dis, c = bfs(b)

print(dis)