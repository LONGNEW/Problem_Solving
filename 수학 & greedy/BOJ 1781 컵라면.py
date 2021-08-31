# import sys
#
# n = int(sys.stdin.readline())
# data = []
# ans = [0] * 200001
#
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     data.append((a, b))
#
# data.sort(key=lambda x:(-x[1]))
# for a, b in data:
#     while ans[a] != 0:
#         a -= 1
#
#     if a == 0:
#         continue
#     ans[a] = b
#
# print(sum(ans))

# import sys
#
# def find_parent(node):
#     if parent[node] != node:
#         parent[node] = find_parent(parent[node])
#
#     return parent[node]
#
# def union(a, b):
#     parent_a = find_parent(a)
#     parent_b = find_parent(b)
#
#     if parent_a < parent_b:
#         parent[b] = parent_a
#     else:
#         parent[a] = parent_b
#
# n = int(sys.stdin.readline())
# data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# ans, parent = [0] * (n + 1), [i for i in range(n + 1)]
#
# data.sort(key=lambda x:(-x[1], -x[0]))
#
# for date, val in data:
#     now_date = find_parent(date)
#
#     if now_date == 0:
#         continue
#
#     union(now_date, now_date - 1)
#     ans[now_date] += val
#
# print(sum(ans))

import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
ans, data = [], [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key=lambda x:x[0])

for date, val in data:
    if len(ans) < date:
        heappush(ans, val)
    else:
        heappush(ans, val)
        heappop(ans)
print(sum(ans))