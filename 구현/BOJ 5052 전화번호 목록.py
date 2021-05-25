import sys

t = int(sys.stdin.readline())
for i in range(t):

    n = int(sys.stdin.readline())
    data = []
    flag = 1

    for j in range(n):
        data.append(sys.stdin.readline().strip())
    data.sort()

    for idx in range(1, len(data)):
        long = data[idx - 1]
        short = data[idx]
        if len(short) > len(long):
            short, long = long, short

        if long[:len(short)] == short:
            flag = 0
            break

    print("YES" if flag else "NO")