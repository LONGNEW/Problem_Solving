import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
target = 1
# 그리디...
# target 의 숫자는 우리가 만드려고 하는 숫자이다.
# data에 존재하는 요소가 이 수보다 작거나 같은 상황이라면 이를 만들 수 있다.
# 그러나 이 보다 크다면 우리는 target 보다 큰 수를 만들어 버리기 때문에
# 그 사이에 공간이 존재한다.
for item in data:
    if target < item:
        break
    target += item
print(target)
