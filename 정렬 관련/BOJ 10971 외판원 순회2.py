import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    data.append(a)


def dfs(start, now, total, visit):
    global ret
    if len(visit) == n:
        if data[now][start] != 0:
            ret = min(ret, total + data[now][start])
        return

    for j in range(n):
        if data[now][j] != 0 and j not in visit:
            visit.append(j)
            dfs(start, j, total + data[now][j], visit)
            visit.pop()


ret = 9999999
for i in range(n):
    dfs(i, i, 0, [i])

print(ret)