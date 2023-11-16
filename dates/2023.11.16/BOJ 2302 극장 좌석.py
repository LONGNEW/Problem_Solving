import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 그림으로 자리 1개 채울 때, 2개 채울 떄, 3개 채울 때를 그려보자.
# 반복되는 구조가 보일 거다.
dp = [0] * 41
dp[1] = 1
dp[2] = 2

for i in range(3, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1
prev = 0
for i in range(m):
    temp = int(sys.stdin.readline())

    # 고정석이랑 그 이전의 자리 사이 공간이 0이면?
    # 1로 유지 해야 함.
    space = temp - prev - 1
    answer *= dp[space] if space != 0 else 1
    prev = temp

space = n - prev
answer *= dp[space] if space != 0 else 1
print(answer)