import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())
edges = [[] for i in range(n + 1)]

for i in range(m):
    h1, h2, k = map(int, sys.stdin.readline().split())
    edges[h1].append((h2, k))
    edges[h2]. append((h1, k))

visit = [-float("inf")] * (n + 1)
q = deque([(s, float("inf"))])
visit[s] = float("inf")
while q:
    pos, cnt = q.popleft()

    if cnt < visit[pos]:
        continue

    for next_pos, limit in edges[pos]:
        carry = min(cnt, limit)
        if visit[next_pos] >= carry:
            continue
        visit[next_pos] = carry
        q.append((next_pos, carry))


print(visit[e] if visit[e] != -float("inf") else 0)
