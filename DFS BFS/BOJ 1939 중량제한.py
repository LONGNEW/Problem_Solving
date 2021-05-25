import sys
from collections import deque

def bfs():
    check = [0] * (n + 1)
    check[start] = 1
    while q:
        now = q.popleft()

        if now == end:
            return 1

        for node, cost in graph[now]:
            if check[node] == 1 or mid > cost:
                continue

            q.append(node)
            check[node] = 1
    return 0

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, sys.stdin.readline().split())

left, right = 1, 1000000000
while left <= right:
    q = deque([start])
    mid = (left + right) // 2

    if bfs() == 0:
        right = mid - 1
    else:
        left = mid + 1

print(right)