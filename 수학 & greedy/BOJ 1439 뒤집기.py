import sys

data = sys.stdin.readline().strip()
zero, one = 0, 0

prev = data[0]
if prev == '1':
    one += 1
else:
    zero += 1

for i in range(1, len(data)):
    if data[i] != prev:
        if data[i] == '1':
            one += 1
        else:
            zero += 1
    prev = data[i]

print(min(zero, one))