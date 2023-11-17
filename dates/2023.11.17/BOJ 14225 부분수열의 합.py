from itertools import combinations

n = int(input())
data = list(map(int, input().split()))
dp = [-1] * 2000000
dp[0] = 0

for i in range(1, n + 1):
    for x in combinations(data, i):
        dp[sum(x)] = 0

print(dp.index(-1))