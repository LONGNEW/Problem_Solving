import sys


def update(idx, val):
    """
        idx위치의 등수를 val로 업데이트
        가장 등수가 높은 애를 저장하기 위해 min을 사용한다.
    """
    while idx <= n:
        tree[idx] = min(tree[idx], val)
        idx += (idx & -idx)


def query(end):
    """
        구간은 1 ~ end로 고정되어 있다.
        각 위치에서 최소값을 찾을 수 있도록 하면 된다.
    """
    ret = float('inf')
    while end > 0:
        ret = min(ret, tree[end])
        end -= (end & -end)

    return ret

n = int(sys.stdin.readline())
student = [[] for _ in range(n + 1)]
tree = [float('inf')] * (n + 1)

student[0] = [0, 0, 0]

for _ in range(3):
    temp = list(map(int, sys.stdin.readline().split()))

    for i in range(1, n + 1):
        num = temp[i - 1]
        student[num].append(i)

student.sort(key=lambda x:x[0])

ans = 0
for i in range(1, n + 1):
    sec_exam, thi_exam = student[i][1], student[i][2]
    former_rank = query(sec_exam)

    if former_rank > thi_exam:
        ans += 1

    update(sec_exam, thi_exam)

print(ans)