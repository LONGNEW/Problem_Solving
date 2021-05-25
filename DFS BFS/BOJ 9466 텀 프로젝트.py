import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())

    graph = [0] + list(map(int, sys.stdin.readline().split()))
    visit = [0] * (n + 1)

    for i in range(1, n + 1):
        pivot = i
        if visit[i] == 0:
            # 연결되는 모든 노드들 일단 동일한 그룹으로 만들자.
            while visit[i] == 0:
                visit[i] = pivot
                i = graph[i]

            # 현재 i는 싸이클이 만들어 졌을 경우 최종 아이템이 들어있다.
            while visit[i] == pivot:
                visit[i] = -1
                i = graph[i]
            
    cnt = 0
    for item in visit:
        if item > 0:
            cnt += 1
    print(cnt)
