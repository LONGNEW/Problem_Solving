import sys

n, m = map(int, sys.stdin.readline().split())
data = dict()
for i in range(n):
    temp = sys.stdin.readline().strip()
    data[temp] = 1

ans = 0
for i in range(m):
    temp = sys.stdin.readline().strip()

    if data.get(temp):
        ans += 1
print(ans)