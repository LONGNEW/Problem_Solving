import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))

    ans = float("inf")
    for min_value in range(1, data[0] + 1):
        max_value = -float("inf")

        for i in range(len(data)):
            pi = min(k, data[i] // min_value)
            max_value = max(max_value, data[i] // pi)

        ans = min(ans, max_value - min_value)

    print(ans)