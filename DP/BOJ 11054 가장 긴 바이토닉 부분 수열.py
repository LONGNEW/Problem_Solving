import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp_subtract = [1] * n
dp_add = [1] * n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp_add[i] = max(dp_add[i], dp_add[j] + 1)

data.reverse()

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp_subtract[i] = max(dp_subtract[i], dp_subtract[j] + 1)

dp_subtract.reverse()
for idx, item in enumerate(dp_add):
    dp_subtract[idx] += item

print(max(dp_subtract) - 1)