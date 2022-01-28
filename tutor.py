import sys, math
from _collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(50000)


class DisjointSet:
    def __init__(self, n):
        self.par = list(range(n + 1))

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x < y:
            self.par[y] = x
        else:
            self.par[x] = y

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]


n, m = map(int, input().split())
D = DisjointSet(n)
adj, edges = [[] for i in range(n)], []

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((c, a, b, i))

edges.sort()
cnt, cost, use = 0, 0, [False] * len(edges)
k = int(math.log2(n)) + 1

for c, a, b, i in edges:
    if D.find(a) != D.find(b):
        use[i] = True

        adj[a].append((b, c))
        adj[b].append((a, c))
        D.union(a, b)

        cost += c
        cnt += 1

if cnt != n - 1:
    print(-1)
    sys.exit()

par = [[-1] * k for i in range(n)]
maxc = [[[-1, -float('inf')] for j in range(k)] for i in range(n)]
d = [-1] * n
d[0] = 0

Q = deque([(0, -1)])
while Q:
    u, p = Q.popleft()
    for v, c in adj[u]:
        if v == p:
            continue

        par[v][0] = u
        maxc[v][0][0] = c
        d[v] = d[u] + 1
        Q.append((v,u))

for i in range(1, k):
    for j in range(n):
        if par[j][i-1] != -1:
            par[j][i] = par[par[j][i-1]][i-1]
            m1, m2 = maxc[j][i-1][0], maxc[par[j][i-1]][i-1][0]
            mm1, mm2 = maxc[j][i-1][1], maxc[par[j][i-1]][i-1][1]
            maxc[j][i][0] = max(m1, m2)

            for mm in (m1, m2, mm1, mm2):
                if mm == maxc[j][i][0]:
                    continue
                maxc[j][i][1] = max(maxc[j][i][1], mm)

newcost = float('inf')
for c, a, b, i in edges:
    if use[i]:
        continue

    if d[a] < d[b]:
        a,b = b,a
    diff = d[a]-d[b]
    cmax =- float('inf')

    i=0
    while diff:
        if diff % 2:
            if maxc[a][i][0]!=c:
                cmax = max(cmax, maxc[a][i][0])
            else:
                cmax = max(cmax, maxc[a][i][1])
            a = par[a][i]
        i+=1
        diff>>=1

    if a != b:
        for i in range(k - 1, -1, -1):

            if par[a][i]!=-1 and par[a][i]!=par[b][i]:

                if maxc[a][i][0] != c:
                    cmax = max(cmax,maxc[a][i][0])
                else:
                    cmax = max(cmax,maxc[a][i][1])

                if maxc[b][i][0] != c:
                    cmax = max(cmax,maxc[b][i][0])
                else:
                    cmax = max(cmax,maxc[b][i][1])
                a = par[a][i]
                b = par[b][i]

        if maxc[a][0][0] != c:
            cmax = max(cmax, maxc[a][0][0])
        else:
            cmax = max(cmax, maxc[a][0][1])

        if maxc[b][0][0] != c:
            cmax = max(cmax, maxc[b][0][0])
        else:
            cmax = max(cmax, maxc[b][0][1])
        a = par[a][0]
    tmp = cost-cmax+c

    if tmp == cost:
        continue
    newcost = min(newcost, tmp)

print(newcost if newcost != float('inf') else -1)