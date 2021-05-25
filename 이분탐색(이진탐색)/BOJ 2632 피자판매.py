import sys
from collections import defaultdict

target = int(sys.stdin.readline())
m, n = map(int, sys.stdin.readline().split())
a, b = [], []

for i in range(m):
    a.append(int(sys.stdin.readline()))
for i in range(n):
    b.append(int(sys.stdin.readline()))

sub_a = defaultdict(int)
sub_a[0] = 1
sub_b = defaultdict(int)
sub_b[0] = 1

for i in range(m):
    temp = 0
    for j in range(m):
        temp += a[(i + j) % m]
        if temp > target:
            break
        else:
            sub_a[temp] += 1

for i in range(n):
    temp = 0
    for j in range(n):
        temp += b[(i + j) % n]
        if temp > target:
            break
        else:
            sub_b[temp] += 1

sub_a[sum(a)] = 1
sub_b[sum(b)] = 1

ans = 0
for key in sub_a:
    aim = target - key
    if sub_b.get(aim):
        ans += sub_a[key] * sub_b[aim]
print(ans)

