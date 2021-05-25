mport sys
from collections import defaultdict

n = int(sys.stdin.readline())
a, b, c, d = [], [], [], []
ab = defaultdict(int)

for i in range(n):
    A, B, C, D = map(int, sys.stdin.readline().split())
    a.append(A)
    b.append(B)
    c.append(C)
    d.append(D)

for num_a in a:
    for num_b in b:
        ab[num_a + num_b] += 1

ans = 0
for num_c in c:
    for num_d in d:
        if ab.get(-(num_c + num_d)):
            ans += ab[-(num_c + num_d)]
print(ans)