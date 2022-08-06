import sys

def adding(th0, th1, th2):
    pivot = max(th0, th2) + 1
    return pivot - th1 if pivot > th1 else 0

def iterate(start, data):
    temp = 0
    for idx in range(start, len(data) - 1, 2):
        temp += adding(data[idx - 1], data[idx], data[idx + 1])
    return temp

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    ans = iterate(1, data)
    if len(data) % 2:
        print(ans)
        continue

    temp = ans
    for i in range(n - 2, 0, -2):
        temp += adding(data[i - 1], data[i], data[i + 1])
        temp -= adding(data[i - 2], data[i - 1], data[i])
        ans = min(temp, ans)
    print(ans)