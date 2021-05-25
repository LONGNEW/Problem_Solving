import sys
from _collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    prime_num = [1] * 10001
    prime_num[1] = 0
    number = []
    i = 2
    while i < 10001:
        cnt = i + i
        while cnt < 10001:
            prime_num[cnt] = 0
            cnt += i
        i += 1

    for i in range(1000, 10001):
        if prime_num[i] == 1:
            number.append(i)

    visit = [0] * len(number)
    q = deque([(n, 0)])

    while q:
        now, cnt = q.popleft()

        if now == k:
            print(cnt)
            break

        now_str = str(now)
        for item in number:
            item_str = str(item)
            idx = number.index(item)
            if now_str[0] != item_str[0] and now_str[1:] == item_str[1:] and visit[idx] == 0:
                visit[idx] = 1
                q.append((item, cnt + 1))
            if now_str[0] == item_str[0] and now_str[1] != item_str[1] and now_str[2:] == item_str[2:] and visit[idx] == 0:
                visit[idx] = 1
                q.append((item, cnt + 1))
            if now_str[:2] == item_str[:2] and now_str[2] != item_str[2] and now_str[3] == item_str[3] and visit[idx] == 0:
                visit[idx] = 1
                q.append((item, cnt + 1))
            if now_str[:3] == item_str[:3] and now_str[3] != item_str[3] and visit[idx] == 0:
                visit[idx] = 1
                q.append((item, cnt + 1))

