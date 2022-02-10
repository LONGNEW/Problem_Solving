import sys

h, w = map(int, sys.stdin.readline().split())
ans = 0

for _ in range(h):
    temp = list(sys.stdin.readline().rstrip())

    left, right = None, None
    for item in temp:
        if left and item != ".":
            ans += 0.5
            left = None
            continue

        if right and item != ".":
            ans += 0.5
            right = None
            continue

        if item == "\\":
            left = 1
            ans += 0.5
            continue

        if item == "/":
            right = 1
            ans += 0.5
            continue

        if left or right:
            ans += 1

print(int(ans))