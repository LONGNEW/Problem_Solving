import sys

def order(in_start, in_end, post_start, post_end):
    # a는 in_order
    # b는 pre_order
    if in_start > in_end or post_start > post_end:
        return

    parents = post_order[-1]


n = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

