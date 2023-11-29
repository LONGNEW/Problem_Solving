import sys

def dfs(node):
    if len(edge[node]) == 0:
        return 1

    ans = 0
    for item in edge[node]:
        ans += dfs(item)
    return ans

n = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
edge = [[] for _ in range(n + 1)]
start = None
delete = int(sys.stdin.readline())

for i in range(n):
    if parent[i] == -1:
        start = i
        continue
    if i == delete:
        continue
    edge[parent[i]].append(i)

if start == delete:
    print(0)
    exit(0)
print(dfs(start))