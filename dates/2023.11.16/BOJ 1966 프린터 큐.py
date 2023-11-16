import sys
from collections import deque

k = int(sys.stdin.readline())

for i in range(k):
    n, m = map(int, sys.stdin.readline().split())
    data = deque([])
    temp = list(map(int, sys.stdin.readline().split()))
    cnt = dict()

    for j in range(len(temp)):
        if temp[j] not in cnt:
            cnt[temp[j]] = 0
        cnt[temp[j]] += 1
        data.append((temp[j], j))

    biggest = sorted(list(cnt.keys()), key=lambda x:-x)
    big_idx = 0

    answer = 0
    while data:
        value, idx_in_temp = data.popleft()

        if value != biggest[big_idx]:
            data.append((value, idx_in_temp))
            continue

        cnt[biggest[big_idx]] -= 1
        if cnt[biggest[big_idx]] == 0:
            big_idx += 1

        answer += 1
        if idx_in_temp == m:
            break
    print(answer)