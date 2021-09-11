import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

idx = n // 2
print(data[idx - 1] if n % 2 == 0 else data[idx])