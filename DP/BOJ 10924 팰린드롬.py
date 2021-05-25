import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [[0] * n for i in range(n)]

for b in range(n):
    for start in range(n):
        end = start + b

        #그냥 구간을 따지자. 어차피 다 돌면서 하면 시간 초과 난다.
        if end >= n:
            break

        if start == end:
            dp[start][end] = 1
            continue

        if start + 1 == end:
            if data[start] == data[end]:
                dp[start][end] = 1
                continue

        #제일 앞 뒤만 같은 지 확인 하고 그 이외의 것은 다른 dp에 저장된 값을 가지고 오자.
        if data[start] == data[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1

m = int(sys.stdin.readline())
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s - 1][e - 1])