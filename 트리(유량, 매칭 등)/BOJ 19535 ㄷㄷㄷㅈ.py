import sys
from collections import defaultdict


def check_g_tree(n):
    return n * (n - 1) * (n - 2) / 6


n = int(sys.stdin.readline())
edge, degree = [], defaultdict(int)
d_cnt, g_cnt = 0, 0

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    degree[u] += 1
    degree[v] += 1
    edge.append((u, v))

for u, v in edge:
    d_cnt += (degree[u] - 1) * (degree[v] - 1)

for key in degree.keys():
    if degree[key] < 3:
        continue
    g_cnt += check_g_tree(degree[key])

if d_cnt > 3 * g_cnt:
    print("D")
elif d_cnt < 3 * g_cnt:
    print("G")
else:
    print("DUDUDUNGA")