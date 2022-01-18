import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, l, k = map(int, sys.stdin.readline().split())
    ids, left, right = [], [], []

    for i in range(n):
        p, a = map(int, sys.stdin.readline().split())

        ids.append(a)
        if a > 0:
            dist = l - p + 1
            right.append(dist)
        else:
            dist = p + 1
            left.append(dist)

    right.sort(reverse=True)
    left.sort()

    move = left + right
    ans = [(move[i], ids[i]) for i in range(n)]

    ans.sort(key=lambda x:(x[0], x[1]))
    print(ans[k - 1][1])