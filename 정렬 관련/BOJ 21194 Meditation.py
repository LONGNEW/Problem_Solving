import sys

k, n = map(int, sys.stdin.readline().split())
data = []
for i in range(k):
    data.append(int(sys.stdin.readline()))
data.sort(key=lambda x:-x)

ans = 0
for i in range(n):
    ans += data[i]
print(ans)