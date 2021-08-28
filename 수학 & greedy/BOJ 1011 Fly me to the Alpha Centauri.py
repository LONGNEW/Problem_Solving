import sys

for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())

    if y - x <= 2:
        print(y - x)
        continue

    diff, ans = 3, 3
    temp, cnt = 2, 0
    while diff <= y - x:
        if cnt == 2:
            cnt = 0
            temp += 1

        diff += temp
        ans += 1
        cnt += 1

    print(ans - 1)