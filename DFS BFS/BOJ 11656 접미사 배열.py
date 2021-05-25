import sys

data = sys.stdin.readline().strip()
items = []
for i in range(len(data)):
    items.append(data[i:])

items.sort()
for item in items:
    print(item)