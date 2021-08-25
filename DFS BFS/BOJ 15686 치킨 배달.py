import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
home, chicken = [], []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))

    for j in range(n):
        if temp[j] == 1:
            home.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))

temp, ans = list(combinations(chicken, m)), float('inf')
for i in range(len(temp)):
    survive = temp[i]
    temp_ans = [float('inf')] * len(home)

    for j in range(len(survive)):
        for k in range(len(home)):
            r1, c1 = survive[j][0], survive[j][1]
            r2, c2 = home[k][0], home[k][1]

            temp_ans[k] = min(temp_ans[k], abs(r1 - r2) + abs(c1 - c2))

    ans = min(sum(temp_ans), ans)

print(ans)