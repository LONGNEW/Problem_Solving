import sys

def dfs(num):
    if dp[num] > 0:
        return dp[num]

    temp = dfs(num - 1) + 1

    if num % 3 == 0:
        temp = min(temp, dfs(num // 3) + 1)
    if num % 2 == 0:
        temp = min(temp, dfs(num // 2) + 1)

    dp[num] = temp
    return dp[num]

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[2], dp[3] = 1, 1

print(dfs(n))

import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])