import sys

n = int(sys.stdin.readline())
previous = 1
current = 2

for i in range(1, n):
    temp = previous
    previous = current
    current = current + temp

print(previous % 15746)