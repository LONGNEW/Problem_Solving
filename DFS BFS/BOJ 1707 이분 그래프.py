import sys
from _collections import deque


def BFS(start):
    global possible
    color[start] = 1
    q = deque([start])

    while q and possible:
        now = q.popleft()

        if visit[now]:
            continue

        visit[now] = True

        for i in graph[now]:
            # 이미 방문을 한 경우에 색깔이 동일한지 판별하는 조건.
            # 방문 했던 노드에 다시 가는 경우에,
            # 사이클이 발생하는 것으로 이를 통해 분류가 가능해진다.
            if visit[i] and color[now] == color[i]:
                possible = False
                break
            # 방문 자체를 하지 않은 경우에는
            # 현재 이 노드가 어떤 색깔을 가지고 있는지 기록해준다.
            elif not visit[i]:
                q.append(i)
                color[i] = -color[now]


t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(n + 1)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = [False] * (n + 1)
    # 이 놈의 컬러가 문제네 ;;
    color = [0] * (n + 1)
    possible = True

    for i in range(1, n + 1):
        # 모든 노드를 확인 해야 하기 때문에
        # for문은 모든 노드에 대해 수행된다.
        if not possible:
            break
        if not visit[i]:
            BFS(i)

    if possible:
        print('YES')
    else:
        print('NO')