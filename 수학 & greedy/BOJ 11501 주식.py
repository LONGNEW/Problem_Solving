import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    max_val = data[-1]
    res = 0
    for j in range(len(data) - 2, -1, -1):
        val = data[j]
        if val > max_val:
            max_val = val
        else:
            res += max_val - val
    print(res)