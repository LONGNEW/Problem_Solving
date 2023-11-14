import sys

n, k = map(int, sys.stdin.readline().split())
list = []

for i in range(1, k + 1):
    temp = str(i * n)
    list.append(int(temp[::-1]))

print(max(list))
