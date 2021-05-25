import sys

def add(idx, num):
    # idx 에 해당하는 놈이 추가 된다.
    while idx < len(tree):
        tree[idx] += num
        idx += (idx & -idx)

def sum(idx):
    ret = 0
    while idx >= 1:
        ret += tree[idx]
        idx &= (idx - 1)
    return ret

def update(idx, num):
    pivot = a[idx]
    a[idx] = num
    while idx < len(tree):
        tree[idx] -= pivot
        tree[idx] += num
        idx += (idx & -idx)


n, m, k = map(int, sys.stdin.readline().split())
tree = [0] * (n + 1)
a = [0] * (n + 1)

for i in range(n):
    temp = int(sys.stdin.readline())
    a[i + 1] = temp
    add(i + 1, temp)

for i in range(m + k):
    k, b, c = map(int, sys.stdin.readline().split())
    if k == 1:
        update(b, c)
    else:
        print(sum(c) - sum(b - 1))