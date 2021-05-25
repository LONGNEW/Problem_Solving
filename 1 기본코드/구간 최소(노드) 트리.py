import sys

def init(array, left, right, node):
    # 기저사례: leaf 노드에 들어오면 그 값을 구간트리에 저장하고, 리턴함.
    if left == right:
        rangeMin[node] = array[left]
        return rangeMin[node]

    mid = (left + right) // 2
    # 왼쪽 자식 구간으로 들어가서 최솟값을 가지고 오도록.
    leftMin = init(array, left, mid, node * 2)
    # 오른쪽 자식 구간으로 들어가서 최솟 값을 가지고 오도록.
    rightMin = init(array, mid + 1, right, node * 2 + 1)
    rangeMin[node] = min(leftMin, rightMin)

    return rangeMin[node]

# 구간의 최소치를 구하는 query 함수
# node의 범위는 nodeLeft, nodeRight. 까지.
# array[left, right]의 교집합의 최소치를 구한다.
def query(left, right, node, nodeLeft, nodeRight):
    # 두 구간에 교집합이 존재하지 않으면(겹치지 않으면) 아주 큰 값을 반환.
    if right < nodeLeft or nodeRight < left:
        return sys.maxsize

    # node가 표현하는 범위가 array[left, right]에 완전히 포함.
    if left <= nodeLeft and nodeRight <= right:
        return rangeMin[node]

    # 양쪽 구간을 찢어야 하면.
    mid = (nodeLeft + nodeRight) // 2
    return min(query(left, right, node * 2, nodeLeft, mid), query(left, right, node * 2 + 1, mid + 1, nodeRight))

# array[index] = newValue로 바뀌었을 때 node를 루트로 하는 구간 트리를 갱신. 노드가 표현하는 구간의 최소치를 반환.
def update(index, newValue, node, nodeLeft, nodeRight)
        # index가 노드가 표현하는 구간과 상관 없는 경우엔 무시.
        if index < nodeLeft or nodeRight > index:
            return rangeMin[node]

        # 트리의 리프까지 왔을 떄.
        if nodeLeft == nodeRight:
            rangeMin[node] = newValue
            return rangeMin[node]

        mid = (nodeLeft + nodeRight) // 2
        rangeMin[node] = min(update(index, newValue, node * 2, nodeLeft, mid),update(index, newValue, node * 2 + 1, mid + 1, nodeRight))
        return rangeMin[node]


n = int(input())
# 배열 데이터를 입력 받자.
data = []
# 구간 트리를 만들기 위해서 길이를 4배한 array를 만든다.
rangeMin = [0] * (4 * n)
