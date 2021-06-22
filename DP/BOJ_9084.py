import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    ans = [0] * 10001
    ans[0] = 1

    for item in coin:
        for j in range(1, 10001):
            if j >= item:
                ans[j] += ans[j - item]

    print(ans[target])