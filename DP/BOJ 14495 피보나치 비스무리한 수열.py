import sys

n = int(sys.stdin.readline())
dp = [-1] * (n + 1)

def recursion(start):
    if start <= 3:
        dp[start] = 1
        return dp[start]
    if dp[start] != -1:
        return dp[start]
    dp[start] = recursion(start - 1) + recursion(start - 3)
    return dp[start]
recursion(n)
print(dp[n])