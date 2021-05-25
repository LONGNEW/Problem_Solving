import sys
sys.setrecursionlimit(10000000)


def eulercircuit(now):
    for i in graph[now]:
        if data[now][i]:
            data[now][i] -= 1
            data[i][now] -= 1

            eulercircuit(i)
    print(now + 1, end=" ")


n = int(sys.stdin.readline())
graph = {}
data = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph[i] = []
    cnt = 0
    for idx, item in enumerate(temp):
        if item == 1:
            graph[i].append(idx)
            cnt += 1

    if cnt % 2 == 1:
        print(-1)
        exit()
    data.append(temp)

eulercircuit(0)