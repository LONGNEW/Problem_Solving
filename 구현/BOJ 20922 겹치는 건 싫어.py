import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

num = [0] * 100001
start, end, length, ans = 0, 0, 0, 0

while start <= end:
    if end == n:
        if length <= ans:
            break
        else:
            num[data[start]] -= 1
            start += 1
            length -= 1

            if num[data[start]] <= k:
                ans = max(ans, length)
        continue

    num[data[end]] += 1
    length += 1
    end += 1

    if num[data[end - 1]] > k:
        while num[data[end - 1]] > k:
            num[data[start]] -= 1
            start += 1
            length -= 1
    else:
        ans = max(ans, length)

print(ans)