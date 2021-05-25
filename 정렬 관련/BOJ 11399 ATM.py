import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

total = 0
waiting = 0
for item in data:
    total += item + waiting
    waiting += item
print(total)