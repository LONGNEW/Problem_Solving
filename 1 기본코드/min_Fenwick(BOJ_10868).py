# fenwick
import sys


def update_tree_start(idx, val):
    """
        제일 앞에서부터 최솟값을 저장해 나가는 방식
        fenwick 트리의 형태를 가지기 때문에 2의 보수 형태를
        더하는 방식으로 각 구간의 최솟값을 저장한다.
    """
    while idx <= n:
        tree_from_start[idx] = min(tree_from_start[idx], val)
        idx += (idx & -idx)

def update_tree_end(idx, val):
    """
            제일 뒤에서부터 최솟값을 저장해 나가는 방식
            fenwick 트리의 형태를 가지기 때문에 2의 보수 형태를
            빼주눈 방식으로 각 구간의 최솟값을 저장한다.
        """
    while idx > 0:
        tree_from_end[idx] = min(tree_from_end[idx], val)
        idx -= (idx & -idx)


def query(a, b):
    """
        a ~ b구간의 최솟값을 리턴 하는 함수
        limit : 특정 2의 완전 제곱수 (a ~ b 구간 사이의 가장 큰 2의 제곱 수)
        a ~ limit, limit ~ b, arr[limit] 중 최솟값을 찾아 리턴 한다.

        논문에서와 같이 tree[0 ~ limit], tree[limit ~ end] 까지의 값이 저장되기 때문에
        이 limit의 경우에는 그냥 배열에서 비교를 해줘야 한다.

        그리고 start에서 만든 트리의 경우 본인이 원하는 a에서부터가 아닌 1에서 부터 시작할 수 있기 때문에
        엇갈려서 최솟값을 찾는다.

        현재 a 에서 부터 최솟값을 찾으려 한다면 tree_end에서 값을 찾고
        b에서부터 찾으려 한다면 tree_start에서 값을 찾아야 한다.
    """
    ret = float('inf')

    cur = a
    cur_parent = cur + (cur & -cur)
    while cur_parent <= b:
        ret = min(ret, tree_from_end[cur])
        # cur_parent의 값을 조정시키기 위해 스왑하는 방식이 필요
        cur = cur_parent
        cur_parent += (cur_parent & -cur_parent)

    cur = b
    cur_parent = cur - (cur & -cur)
    while cur_parent >= a:
        ret = min(ret, tree_from_start[cur])
        # cur_parent의 값을 조정시키기 위해 스왑하는 방식이 필요
        cur = cur_parent
        cur_parent -= (cur_parent & -cur_parent)

    # 마지막으로 들어가지 못했던 cur 인덱스의 값 그자체를 비교한다.
    # 구역을 물어봤을 때 포함하지 않는 구역이 있었기 때문에 원소
    # 그 자체를 비교해야 함
    ret = min(ret, arr[cur])
    return ret


n, m = map(int, sys.stdin.readline().split())
arr = [0] * (n + 1)
tree_from_start = [float('inf')] * (n + 1)
tree_from_end = [float('inf')] * (n + 1)

for i in range(1, n + 1):
    arr[i] = int(sys.stdin.readline())
    update_tree_start(i, arr[i])
    update_tree_end(i, arr[i])

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(query(a, b))
