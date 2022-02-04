import sys

n, m = map(int, sys.stdin.readline().split())
data = dict()

for _ in range(n):
    a, b = sys.stdin.readline().split()
    data[a] = b

for _ in range(m):
    print(data[sys.stdin.readline().rstrip()])