import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
ret = 0

for i in range(len(data) - 1):
    target = max(data)
    target_idx = data.index(target)
    if target_idx == 0:
        ret += target - data[1]
    elif target_idx == len(data) - 1:
        ret += target - data[-2]
    else:
        ret = min(ret + target - data[target_idx - 1], ret + target - data[target_idx + 1])

    del data[target_idx]

print(ret)