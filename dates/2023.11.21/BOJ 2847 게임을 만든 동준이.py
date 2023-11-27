import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    temp = int(sys.stdin.readline())
    data.append(temp)

answer = 0
for i in range(n - 1, 0, -1):
    if data[i - 1] >= data[i]:
        answer += data[i - 1] - data[i] + 1
        data[i - 1] = data[i] - 1
print(answer)