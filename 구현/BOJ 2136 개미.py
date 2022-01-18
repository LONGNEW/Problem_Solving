import sys

n, l = map(int, sys.stdin.readline().split())
ids, left, right = [], [], []

for i in range(n):
    pos = int(sys.stdin.readline())

    ids.append((abs(pos), i + 1))
    if pos > 0:
        right.append(l - pos)
    else:
        left.append(-pos)

ids.sort()
left.sort()
right.sort(reverse=True)

move = left + right
ans = [(move[i], ids[i][1]) for i in range(n)]

ans.sort()
print(ans[-1][1], ans[-1][0])