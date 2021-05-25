import sys

n, l = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort()

start = data[0] - 0.5
end = start + l
ans = 1

for i in range(1, n):
    if end < data[i] + 0.5:
        start = data[i] - 0.5
        end = start + l
        ans += 1
print(ans)