import sys
sys.setrecursionlimit(1000000)

def pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    print(root)
    mid = position[root]

    # in_order 기준으로 왼쪽 아이템이 얼마나 존재하는지 확인
    left = mid - in_start
    # in_order의 경우에는 mid를 기준으로 좌우가 나뉘게 된다.
    # post_order는?
    # in_order 배열에서 좌, 우에 존재하는 요소의 갯수를 세아린 것을 이용해서.
    # 현재 시작점 + (in_) 좌측에 존재하는 아이템 갯수 - 1 까지.
    # 그러고 나서 좌측에 ~ post_end - 1(root를 빼주는것) 을 하면 된다.
    # in_order 에서 나뉘는 아이템 갯수를 이용해서 해야 한다고 생각하고 있었는데
    # 이것을 이렇게 써먹는 군...
    pre_order(in_start, mid - 1, post_start, post_start + left - 1)
    pre_order(mid + 1, in_end, post_start + left, post_end - 1)



n = int(sys.stdin.readline().strip())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))
position = {}
for i in range(n):
    position[in_order[i]] = i

pre_order(0, len(post_order) - 1, 0, len(post_order) - 1)