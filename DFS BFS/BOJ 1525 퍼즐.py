import sys
from _collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dist = dict()
aa = ''

for i in range(3):
    a = sys.stdin.readline().strip().replace(' ', '')
    aa += a

aa = int(aa.replace('0', '9'))
nothing = 1
q = deque()
q.append(aa)
dist[aa] = 0

while q:
    status = q.popleft()
    if status == 123456789:
        print(dist[status])
        nothing = 0
        break

    status_str = str(status)
    where = status_str.find('9')
    x, y = where // 3, where % 3

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 3 or nx < 0 or ny >= 3 or ny < 0:
            continue
        # 문자열에서 위치 찾기.
        target = nx * 3 + ny
        temp = list(status_str)
        temp[where], temp[target] = temp[target], temp[where]
        temp = int("".join(temp))

        if  temp not in dist.keys():
            dist[temp] = dist[status] + 1
            q.append(temp)

if nothing:
    print(-1)