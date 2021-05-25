import sys


def five(a):
    ret = 0
    while a != 0:
        a //= 5
        ret += a
    return ret


def two(a):
    ret = 0
    while a != 0:
        a //= 2
        ret += a
    return ret


n, m = map(int, sys.stdin.readline().split())
if m == 0:
    print(0)
else:
    print(min(two(n) - two(m) - two(n - m), (five(n) - five(m) - five(n - m))))