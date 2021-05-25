import sys

n = int(sys.stdin.readline())
positive = []
negative = []
one = 0
for i in range(n):
    data = int(sys.stdin.readline())
    if data > 1:
        positive.append(data)
    elif data <= 0:
        negative.append(data)
    else:
        one += 1

positive.sort(reverse=True)
negative.sort()

ans = 0
for i in range(0, len(positive), 2):
    if i + 1 < len(positive):
        ans += positive[i] * positive[i + 1]
    else:
        ans += positive[i]
for i in range(0, len(negative), 2):
    if i + 1 < len(negative):
        ans += negative[i] * negative[i + 1]
    else:
        ans += negative[i]


print(ans + one)
