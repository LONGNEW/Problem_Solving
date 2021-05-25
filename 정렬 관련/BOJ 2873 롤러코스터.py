import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

ret = ''
front = ''
back = ''
if n % 2 == 1:
    ret += (('R' * (m - 1) + 'D') + ('L' * (m - 1) + 'D')) * (n // 2) + 'R' * (m - 1)
elif m % 2 == 1:
    ret += (('D' * (n - 1) + 'R') + ('U' * (n - 1) + 'R')) * ((n - 1) // 2) + 'D' * (n - 1)
else:
    score = 999
    x, y = -1, -1
    for i in range(0, n, 2):
        for j in range(1, m, 2):
            if score > graph[i][j]:
                x = i
                y = j
                score = graph[i][j]
    for i in range(1, n, 2):
        for j in range(0, m, 2):
            if score > graph[i][j]:
                x = i
                y = j
                score = graph[i][j]
    front += (('R' * (m - 1) + 'D') + ('L' * (m - 1) + 'D')) * (x // 2)
    back += (('D' + 'L' * (m - 1)) + ('D' + 'R' * (m - 1))) * ((n - x - 1) // 2)
    if y % 2 == 0:
        front += 'DRUR' * (y // 2) + 'RD'
        back = 'RURD' * ((m - y - 2) // 2) + back
    else:
        front += 'DRUR' * ((y - 1) // 2) + 'DR'
        back = 'RURD' * ((m - y - 1) // 2) + back
    ret = front + back
print(ret