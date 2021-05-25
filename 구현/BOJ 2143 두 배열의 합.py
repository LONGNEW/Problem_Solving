import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a_sub, b_sub = {}, {}
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += a[j]
        if a_sub.get(temp):
            a_sub[temp] += 1
        else:
            a_sub[temp] = 1

for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += b[j]
        if b_sub.get(temp):
            b_sub[temp] += 1
        else:
            b_sub[temp] = 1

ans = 0
for value in a_sub:
    if b_sub.get(t - value):
        ans += (a_sub[value] * b_sub[t - value])
print(ans)