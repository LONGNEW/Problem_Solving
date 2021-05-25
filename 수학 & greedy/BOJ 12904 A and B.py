import sys

target = list(sys.stdin.readline().strip())
data = list(sys.stdin.readline().strip())

while len(data) > len(target):
    if data[-1] == "A":
        data.pop()
    else:
        data.pop()
        data.reverse()

print(1 if data == target else 0)