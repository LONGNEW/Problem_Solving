import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

start, end, cnt, length = 0, 0, 0, 0
ans = float('inf')

while start <= end:
    if end == n:
        if cnt < k:
            break
        ans = min(ans, length)
        if data[start] == 1:
            cnt -= 1
        length -= 1
        start += 1
        continue

    if cnt < k:
        if data[end] == 1:
            cnt += 1
        length += 1
        end += 1
    else:
        ans = min(ans, length)
        if data[start] == 1:
            cnt -= 1
        length -= 1
        start += 1
print(-1 if ans == float('inf') else ans)