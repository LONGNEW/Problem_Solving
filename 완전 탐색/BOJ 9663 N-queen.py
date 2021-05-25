import sys

n, ans = int(input()), 0
# 세로, 행에 대한 위치를 기록하기 위함.
vertical = [False] * n
# 왼쪽 아래에서 오른쪽 위로 상승하는 대각선의 모양을 기록.
# 이 위치들이 수가 동일하게 가기 때문에. 추가적인 설명은 레바스 님의 글을 보자.
# 그림에서 같은 대각선에 존재하는 경우에 동일한 값을 가지고 있어서.
# 1차원 배열로 이를 나타낼수 있다.
right_upper = [False] * (2 * n - 1)
right_lower = [False] * (2 * n - 1)

def solve(row):
    global ans
    # 현재의 행이 n과 동일 하면, 모든 퀸을 배치 한 것이다.
    if row == n:
        ans += 1
        return

    for col in range(n):
        # 모든 행에서 '모든' 열에다가 퀸을 놓아 보기 때문에 완전 탐색을 하는 것이라 볼수 있다.
        # 그리고 모든 배열의 값들이 False 여야 하는데 이미 True 라면,
        # 다른 Queen의 이동범위에 들어가는 것이기 때문이다.
        # 여기서 들었던 의문 가로로 움직이는 건 그냥 무시?
        # 그냥 무시가 아닌, 우리는 지금 현재 존재하는 행에서 모든 열에 퀸을 놓을 것이다.
        # 그러니까 동일 한 행에 다른 퀸을 놓을 경우 자체가 존재 하지 않는다.
        # 그러한 이유로 우리는 세로, 대각선 2개의 경우만 따지면 된다.
        if not (vertical[col] or right_upper[row + col] or right_lower[row - col + n - 1]):
            vertical[col] = right_upper[row + col] = right_lower[row - col + n - 1] = True
            solve(row + 1)
            # 살짝 dfs를 할 떄 처럼 재귀를 수행하고 나서는 다시 그 위치들을 False로 업데이트 한다.
            vertical[col] = right_upper[row + col] = right_lower[row - col + n - 1] = False

solve(0)
print(ans)
