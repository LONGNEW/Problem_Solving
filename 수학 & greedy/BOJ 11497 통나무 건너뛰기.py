import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()

    ans = -99999

    for j in range(2, n):
        ans = max(ans, abs(data[j - 2] - data[j]))

    print(ans)