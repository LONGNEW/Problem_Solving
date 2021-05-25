import sys

n = int(sys.stdin.readline())
data = []
ans = [0] * 200001

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))

data.sort(key=lambda x:(-x[1]))
for a, b in data:
    while ans[a] != 0:
        a -= 1

    if a == 0:
        continue
    ans[a] = b

print(sum(ans))