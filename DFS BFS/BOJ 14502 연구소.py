import sys
from itertools import combinations
from _collections import deque

n, m = map(int, sys.stdin.readline().split())
data = []
temp = [[0] * m for _ in range(n)]
virus = []
empty = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if a[j] == 2:
            virus.append((i, j))
        if a[j] == 0:
            empty.append((i, j))
    data.append(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ret = 0

def viruses():
    q = deque()
    for item in virus:
        q.append(item)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))

def zeros():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt


for positions in combinations(empty, 3):
    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]

    for now_x, now_y in positions:
        temp[now_x][now_y] = 1

    viruses()
    ret = max(ret, zeros())

print(ret)

-----------------------------------------------------------

import sys

n, m = map(int, sys.stdin.readline().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ret = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx, ny)

def zeros():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

def wall(count):
    global ret
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        ret = max(ret, zeros())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                wall(count)
                data[i][j] = 0
                count -= 1

wall(0)
print(ret)