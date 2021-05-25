from _collections import deque
import sys
N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

dis = [-1] * (N + 1)
dis[X] = 0
q = deque([X])

while q:
    node = q.popleft()
    for next_node in graph[node]:
        if dis[next_node] == -1:
            dis[next_node] = dis[node] + 1
            q.append(next_node)

check = False
for i in range(1, len(dis)):
    if dis[i] == K:
        print(i)
        check = True

if not check:
    print(-1)