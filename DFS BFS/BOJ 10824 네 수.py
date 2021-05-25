import sys

data = sys.stdin.readline().split()
front = data[0] + data[1]
back = data[2] + data[3]
print(int(front) + int(back))