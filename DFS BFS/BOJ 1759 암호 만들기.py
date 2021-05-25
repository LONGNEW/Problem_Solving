import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
alpha = list(sys.stdin.readline().split())
a = []
b = []
ret = set()

for item in alpha:
    if item in ('a', 'e', 'o', 'i', 'u'):
        a.append(item)
    else:
        b.append(item)

for i in range(1, len(a) + 1):
    for mouem in combinations(a, i):
        if l - i >= 2:
            for jauem in combinations(b, l - i):
                temp = mouem + jauem
                temp = sorted(temp)
                temp = "".join(temp)
                ret.add(temp)
ret = sorted(ret)
for i in ret:
    print(i)