import sys


def update(idx, val):
    update_start(idx, val)
    update_end(idx, val)


def update_start(idx, val):
    while idx <= n:
        tree_start[idx] = min(tree_start[idx], val)
        idx += (idx & -idx)


def update_end(idx, val):
    while idx > 0:
        tree_end[idx] = min(tree_end[idx], val)
        idx -= (idx & -idx)


def query(start, end):
    ret = float('inf')

    cur = start
    cur_parent = cur + (cur & -cur)
    while cur_parent <= end:
        ret = min(ret, tree_end[cur])
        cur = cur_parent
        cur_parent += (cur_parent & -cur_parent)

    cur = end
    cur_parent = cur - (cur & -cur)
    while cur_parent >= start:
        ret = min(ret, tree_start[cur])
        cur = cur_parent
        cur_parent -= (cur_parent & -cur_parent)

    ret = min(ret, data[cur])
    return ret


n, m = map(int, sys.stdin.readline().split())
tree_start, tree_end = [float('inf')] * (n + 1), [float('inf')] * (n + 1)
data = [0] * (n + 1)

for i in range(1, n + 1):
    data[i] = int(sys.stdin.readline())
    update_start(i, data[i])
    update_end(i, data[i])

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    print(query(a, b))