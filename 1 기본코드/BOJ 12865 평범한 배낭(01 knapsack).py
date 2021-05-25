import sys

n, k = map(int, sys.stdin.readline().split())
data = []
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    data.append((w, v))

# 바로 이전 값을 저장해놓는 DP 용
temp = [0] * (k + 1)
ans = [0] * (k + 1)

for wei, val in data:
    # 기준이 되는 w (배낭 무게) 임.
    for w in range(k + 1):
        if wei > w:
            ans[w] = temp[w]
        else:
            ans[w] = max(val + temp[w - wei], temp[w])

    for idx, item in enumerate(ans):
        temp[idx] = item

print(ans[-1])