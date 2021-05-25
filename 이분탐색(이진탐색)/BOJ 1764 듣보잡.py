import sys

n, m = map(int, sys.stdin.readline().split())
data_1 = []
data_2 = dict()
for i in range(n):
    name = sys.stdin.readline().strip()
    data_1.append(name)

for i in range(m):
    name = sys.stdin.readline().strip()
    data_2[name] = 1

ans = []
for name in data_1:
    if data_2.get(name):
        ans.append(name)

ans.sort()
print(len(ans))
for name in ans:
    print(name)

import sys

N, M = map(int, sys.stdin.readline().split())
data_1 = [sys.stdin.readline().strip() for i in range(N)]
data_2 = [sys.stdin.readline().strip() for i in range(M)]

# 교차하는 이름들을 찾는다
ans = sorted(list(set(data_1) & set(data_2)))

print(len(ans))
for name in ans:
    print(name)