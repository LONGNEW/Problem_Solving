import sys

n = int(sys.stdin.readline())

previous = [0, 1]
current = [0, 0]

for i in range(n - 1):
    current[0] = previous[1]
    current[0] += previous[0]
    current[1] = previous[0]

    previous[0] = current[0]
    previous[1] = current[1]

print(sum(previous))