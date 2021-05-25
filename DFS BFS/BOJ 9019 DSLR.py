import sys
from _collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    dp = [-1] * 10001

    if len(str(a)) < 4:
        a = str(a).zfill(4)

    q = deque([(a, '')])
    dp[int(a)] = 1

    while q:
        now_str, command = q.popleft()
        if type(now_str) != str:
            now_str = str(now_str)
        now = int(now_str)

        if now == b:
            print(command)
            break

        next_num = (now * 2) % 10000
        next_str = str(next_num)
        if dp[next_num] == -1:

            if next_num < 1000:
                next_str = next_str.zfill(4)

            dp[next_num] = 1
            q.append((next_str, command + 'D'))

        next_num = (now - 1) % 10000
        next_str = str(next_num)
        if dp[next_num] == -1:

            if next_num < 1000:
                next_str = next_str.zfill(4)

            dp[next_num] = 1
            q.append((next_str, command + 'S'))

        next_str = now_str[1:] + now_str[0]
        next_num = int(next_str)
        if dp[next_num] == -1:
            dp[next_num] = 1
            q.append((next_str, command + 'L'))

        next_str = now_str[3] + now_str[:3]
        next_num = int(next_str)
        if dp[next_num] == -1:
            dp[next_num] = 1
            q.append((next_str, command + 'R'))