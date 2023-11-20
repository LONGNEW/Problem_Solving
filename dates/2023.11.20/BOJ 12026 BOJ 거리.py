import sys

n = int(sys.stdin.readline())
data = list(sys.stdin.readline().strip())
next_step = {
    "B": "O",
    "O": "J",
    "J": "B"
}

dp = [float("inf")] * n
dp[0] = 0
for pos in range(n - 1):
    if data[pos] == float("inf"):
        continue

    alpha = data[pos]
    cnt = 0
    for j in range(pos + 1, n):
        if next_step[alpha] == data[j]:
            cnt += 1
            dp[j] = min(dp[j], dp[pos] + (j - pos) ** 2)

    if cnt != 0:
        alpha = next_step[alpha]

if dp[-1] == float("inf"):
    print(-1)
else:
    print(dp[-1])