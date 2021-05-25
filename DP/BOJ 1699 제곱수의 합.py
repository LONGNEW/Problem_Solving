import sys

N = int(sys.stdin.readline())
data = [i * i for i in range(1, 320)]
dp = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    s = []

    for j in data:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[N])