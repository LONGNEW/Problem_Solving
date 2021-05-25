N, M= map(int, sys.stdin.readline().split())
time = list(map(int, sys.stdin.readline().split()))

low = 1
high = 1000000000000

while low + 1 < high:
    mid = (high + low) // 2
    cnt = 0
    for spend in time:
        cnt += (mid // spend)
    if cnt >= M:
        high = mid
    else:
        low = mid
print(high)