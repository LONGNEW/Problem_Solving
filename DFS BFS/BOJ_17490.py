import sys

n, m, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
pos = []
flag = 0

if m <= 1:
    print("YES")
    exit(0)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if a == n and b == 1:
        flag = 1
        continue

    if a > b:
        a, b = b, a
    pos.append(a)

pos.sort()
ans, now = 0, 0
first = min(data[now:pos[0]])

for item in pos:
    temp = data[now: item]
    ans += min(temp)
    now = item

if flag == 0:
    temp = data[now:]
    last = min(temp)
    if last < first:
        ans -= first
        ans += last
else:
    ans += min(data[now:])

if ans > k:
    print("NO")
else:
    print("YES")