import sys

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
ans = float("inf")

start, end = 0, 0
temp = data[0]

while True:
    if start > end:
        end = start + 1

        if end < n:
            temp += data[end]
        continue

    if temp >= s:
        ans = min(ans, end - start + 1)
        temp -= data[start]
        start += 1
        continue

    end += 1
    if end >= n:
        break
    temp += data[end]


print(0 if ans == float("inf") else ans)