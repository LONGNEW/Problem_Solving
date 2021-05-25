import sys
from _collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
visit = [-1] * (N + 1)

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

q = deque([1])
visit[1] = 1
cnt = 0
while q:
    node = q.popleft()
    cnt += 1
    for next_node in graph[node]:
        if visit[next_node] != 1:
            q.append(next_node)
            visit[next_node] = 1

print(cnt - 1)