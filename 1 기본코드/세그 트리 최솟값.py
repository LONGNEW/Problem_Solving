def init():
    elem_idx = int(pow(2, height - 1))
    for i in range(n):
        idx = elem_idx + i
        tree[idx] = data[i]

    for i in range(elem_idx - 1, 0, -1):
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])

# s : search, t : target
def query(tree_idx, s_l, s_r, t_l, t_r):
    if tree_idx <= 0 or tree_idx >= length:
        return float("inf")
    if s_r < t_l or s_l > t_r:
        return float("inf")
    if t_l <= s_l and s_r <= t_r:
        return tree[tree_idx]

    mid = (s_l + s_r) // 2
    left = query(tree_idx * 2, s_l, mid, t_l, t_r)
    right = query(tree_idx * 2 + 1, mid + 1, s_l, t_l, t_r)

    return min(left, right)