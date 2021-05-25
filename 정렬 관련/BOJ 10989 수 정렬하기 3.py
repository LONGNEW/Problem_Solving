import sys

n = int(sys.stdin.readline())
data = [0] * 10001
for i in range(n):
    temp = int(sys.stdin.readline())
    data[temp] += 1

for i in range(1, 10001):
    print('{0}\n'.format(i) * data[i], end="")