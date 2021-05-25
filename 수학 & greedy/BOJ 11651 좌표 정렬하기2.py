import sys

n = int(sys.stdin.readline())
position = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    position.append((x, y))

position = sorted(position, key=lambda x : (x[1], x[0]))

for item in position:
    print(*item)