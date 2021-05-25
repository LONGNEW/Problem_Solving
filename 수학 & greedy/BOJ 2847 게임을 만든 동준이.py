import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))

ans = 0

for i in range(n - 2, -1, -1):
    prev = data[i + 1]
    now = data[i]
    if now >= prev:
        ans += now - prev + 1
        data[i] = now - now + prev - 1

print(ans)