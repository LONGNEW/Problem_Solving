import sys

ans = [0] * 10001
n = int(sys.stdin.readline())
data = []
for i in range(n):
    p, d = map(int, sys.stdin.readline().split())
    data.append((p, d))

data.sort(key= lambda x:-x[0])
for p, d in data:
    while ans[d] != 0:
        d -= 1

    if d != 0:
        ans[d] = p

print(sum(ans))