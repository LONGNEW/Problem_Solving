import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        data.pop()
        continue
    data.append(temp)

print(sum(data))