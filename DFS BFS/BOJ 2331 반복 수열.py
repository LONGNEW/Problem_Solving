import sys

a, p = map(int, sys.stdin.readline().split())
data = [a]
cycle = []

for i in range(10000):
    num = data[i]
    next_num = 0
    while num > 0:
        next_num += (num % 10) ** p
        num = num // 10
    data.append(next_num)
idx = 0
while True:
    if data[idx] in data[idx + 1:]:
        break
    cycle.append(data[idx])
    idx += 1
print(len(cycle))
