import sys

first = [0] + list(sys.stdin.readline().rstrip())
second = [0] + list(sys.stdin.readline().rstrip())

data = [[""] * len(second) for i in range(len(first))]

for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]:
            data[i][j] = data[i - 1][j - 1] + first[i]
            continue

        if len(data[i][j - 1]) > len(data[i - 1][j]):
            data[i][j] = data[i][j - 1]
        else:
            data[i][j] = data[i - 1][j]

print(len(data[len(first) - 1][len(second) - 1]))
print(data[len(first) - 1][len(second) - 1])
