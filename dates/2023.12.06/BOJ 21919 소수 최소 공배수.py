import math
import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

check = [0] * (max(data) + 1)

for i in range(2, len(check)):
    flag = 1
    for target in range(2, int(math.sqrt(i)) + 1):
        if i % target == 0:
            flag = 0
            break
    check[i] = flag

ans = 1
used = [1] * (max(data) + 1)
for idx in data:
    if check[idx] and used[idx]:
        ans *= idx
        used[idx] = 0

print(-1 if ans == 1 else ans)