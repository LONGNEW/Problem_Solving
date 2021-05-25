import sys

n = int(sys.stdin.readline())

previous = 0
current = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        temp = current
        current += previous
        previous = temp
    print(current)