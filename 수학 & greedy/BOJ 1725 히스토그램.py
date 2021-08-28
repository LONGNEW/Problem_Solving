import sys

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]

ans, height = -float('inf'), []
for i in range(len(data)):

    start_idx = -1
    while height and height[-1][0] > data[i]:
        value, start_idx = height.pop()
        ans = max(value * (i - start_idx), ans)

    if start_idx != -1:
        height.append([data[i], start_idx])
        continue

    height.append([data[i], i])

left = len(height)
for i in range(len(height)):
    ans = max(height[i][0] * (n - height[i][1]), ans)

print(ans)