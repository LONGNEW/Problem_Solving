import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))

minimum = oil[0]
ans = 0

for idx in range(len(distance)):
    if oil[idx] < minimum:
        minimum = oil[idx]
    ans += minimum * distance[idx]

print(ans)