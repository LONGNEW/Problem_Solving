import sys

def sum(pos):
    ret = 0

    while pos > 0:
        ret += tree[pos]
        pos = pos & (pos - 1)

    return ret

def update(pos):
    while pos <= n:
        tree[pos] += 1
        pos += (pos & -pos)

n = int(sys.stdin.readline())
data, tree = [], [0] * (n + 1)

for i in range(n):
    temp = int(sys.stdin.readline())
    data.append([temp, i])

data.sort()
for i in range(1, n + 1):
    data[i - 1][0] = i

data.sort(key=lambda x:x[1])
for i in range(1, n + 1):
    val, idx = data[i - 1]
    print(i - sum(val))
    update(val)