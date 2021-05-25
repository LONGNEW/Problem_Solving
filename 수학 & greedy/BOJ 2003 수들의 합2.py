import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(0, len(data)):
    total = 0
    for j in range(i, len(data)):
        total += data[j]
        if total == m:
            ans += 1
            break
        if total > m:
            break
print(ans)
