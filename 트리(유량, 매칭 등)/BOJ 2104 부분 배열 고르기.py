import sys
sys.setrecursionlimit(100000)

def init(idx, left, right):
    if left == right:
        tree[idx] = (data[left], left)
        return tree[idx]

    mid = (left + right) // 2
    lsum, lidx = init(idx * 2, left, mid)
    rsum, ridx = init(idx * 2 + 1, mid + 1, right)

    tree[idx] = (lsum + rsum, lidx if data[lidx] < data[ridx] else ridx)
    return tree[idx]

# s : search, t : target
def query(idx, sl, sr, tl, tr):
    if tr < sl or sr < tl:
        return (0, 0)
    if tl <= sl and sr <= tr:
        return tree[idx]

    mid = (sl + sr) // 2
    lsum, lidx = query(idx * 2, sl, mid, tl, tr)
    rsum, ridx = query(idx * 2 + 1, mid + 1, sr, tl, tr)

    ret = (lsum + rsum, lidx if data[lidx] < data[ridx] else ridx)
    return ret

def pick(left, right):
    if left == right:
        return data[left] * data[right]

    min_sum, idx = query(1, 1, n, left, right)
    ret = min_sum * data[idx]
    if left <= idx - 1:
        ret = max(ret, pick(left, idx - 1))
    if idx + 1 <= right:
        ret = max(ret, pick(idx + 1, right))
    return ret

n = int(sys.stdin.readline())
tree = [(0, 0)] * (100001 * 4)

data = [0] * 100001
data[0] = float("inf")
for idx, item in enumerate(list(map(int, sys.stdin.readline().split()))):
    data[idx + 1] = item

init(1, 1, n)
print(pick(1, n))