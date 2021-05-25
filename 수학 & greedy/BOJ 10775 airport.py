import sys
def union(a, b):
    # a번 게이트에 도킹을 하면 그 게이트에 다음 비행기가 오면
    # 이것은 a - 1번 게이트에 도킹을 하게 된다.
    # 이를 모든 배열에 적용시키기 위해 union-find를 사용.
    parent_a = find(a)
    parent_b = find(b)

    data[parent_a] = parent_b

def find(x):
    if x == data[x]:
        return x

    data[x] = find(data[x])
    return data[x]

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
ans = 0

data = [i for i in range(g + 1)]

for i in range(p):
    gate = int(sys.stdin.readline())

    where = find(gate)
    # 현재 gate에 도킹이 가능한가를 판별해야함.
    # 이 gate의 부모가 0에 존재한다면 더 이상 도킹이 불가.
    if where == 0:
        break

    union(where, where - 1)
    ans += 1

print(ans)