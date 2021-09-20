"""
    아이템 사이 구매 순서. -> 위상 정렬

"""
import sys
from collections import deque

n = int(sys.stdin.readline())
indexs, data = dict(), dict()

for i in range(n):
    a, b = sys.stdin.readline().split()

    if a not in data:
        data[a] = []
        indexs[a] = 0

    if b not in data:
        data[b] = []
        indexs[b] = 0

    data[a].append(b)
    indexs[b] += 1

q = []
for item in list(indexs.keys()):
    if indexs[item] == 0:
        q.append((item, data[item]))
        del indexs[item]
        del data[item]

ans = []
q.sort()
temp = deque(q)
while temp:
    q = []
    limit = len(temp)

    for i in range(limit):
        now = temp.popleft()

        ans.append(now[0])
        for item in now[1]:
            indexs[item] -= 1

            if indexs[item] == 0:
                q.append((item, data[item]))
                del indexs[item]
                del data[item]

    q.sort()
    temp = deque(q)

if len(indexs) > 0:
    print(-1)
    exit(0)

for item in ans:
    print(item)

