import sys

n, m = map(int, sys.stdin.readline().split())
data = []

for i in range(n):
    wei, val = map(int, sys.stdin.readline().split())
    data.append((wei, val))

ans = [0] * m
weight = [int(sys.stdin.readline()) for _ in range(m)]
bag_wei = max(weight)

prev = [0] * (bag_wei + 1)
now = [0] * (bag_wei + 1)
for stone_wei, stone_val in data:

    for j in range(stone_wei, bag_wei + 1):
        now[j] = max(prev[j - stone_wei] + stone_val, now[j])

    for j in range(len(prev)):
        prev[j] = now[j]

for i in range(m):
    ans[i] = now[weight[i]] / weight[i]

ret = ans.index(max(ans))
print(ret + 1)