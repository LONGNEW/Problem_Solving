import sys
import itertools

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

permutation = itertools.permutations(data, n)

ret = -9999
for item in permutation:
    cnt = 0
    l_idx = 0
    r_idx = n - 1
    while l_idx < r_idx:
        cnt += abs(item[l_idx] - item[r_idx])
        l_idx += 1
        if l_idx == r_idx:
            break
        cnt += abs(item[l_idx] - item[r_idx])
        r_idx -= 1
    ret = max(ret, cnt)
print(ret)
