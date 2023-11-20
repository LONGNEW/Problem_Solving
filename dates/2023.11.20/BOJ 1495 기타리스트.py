n, s, m = map(int, input().split())
data = list(map(int, input().split()))
dp = [0] * (m + 1)
dp[s] = 1

for i in range(n):
    up_low = data[i]
    temp_dp = [0] * (m + 1)

    for j in range(m + 1):
        if dp[j] != 1:
            continue

        if j + up_low < m + 1:
            temp_dp[j + up_low] = 1
        if j - up_low >= 0:
            temp_dp[j - up_low] = 1

    dp = temp_dp

for i in range(m, -1, -1):
    if dp[i] == 1:
        print(i)
        exit(0)
print(-1)