import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    one, two = map(int, sys.stdin.readline().split())
    graph[one].append(two)
    graph[two].append(one)

if a == b:
    print(0)
    exit()

visit = [0] * (n + 1)
visit[a] = 1

q = deque([(a, 0)])
while q:
    now, cnt = q.popleft()

    for next_node in graph[now]:
        if next_node == b:
            print(cnt + 1)
            exit()

        if visit[next_node] == 0:
            visit[next_node] = 1
            q.append((next_node, cnt + 1))

print(-1)