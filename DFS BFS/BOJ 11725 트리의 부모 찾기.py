import sys
from _collections import deque

n = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
parent = [i for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS():
    start = 1
    q = deque([start])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if parent[next_node] == next_node:
                parent[next_node] = now
                q.append(next_node)

BFS()
for i in range(2, len(parent)):
    print(parent[i])
