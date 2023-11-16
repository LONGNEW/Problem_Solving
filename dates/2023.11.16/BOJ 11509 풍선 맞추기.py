import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
stack = dict()

for i in range(n - 1, -1, -1):
    height = data[i]
    if height - 1 in stack and stack[height - 1] > 0:
        stack[height - 1] -= 1

    if height not in stack:
        stack[height] = 0
    stack[height] += 1

answer = 0
for key in stack.keys():
    answer += stack[key]
print(answer)