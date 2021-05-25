import sys

n = int(sys.stdin.readline())
result = []

def hanoi(disk, from_, to):
    if disk == 1:
        result.append((from_, to))
    else:
        other_poll = 6 - from_ - to

        hanoi(disk - 1, from_, other_poll)
        result.append((from_, to))
        hanoi(disk - 1, other_poll, to)

hanoi(n, 1, 3)
print(len(result))
for item in result:
    print(item[0], item[1])