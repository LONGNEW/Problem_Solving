from _collections import deque

node, edge_num = map(int, input().split())
#진입차수의 초기화가 필요하다
indegree = [0] * (node + 1)
graph = [[] for i in range(node + 1)]

for _ in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    #정렬된 값들을 담을 리스트
    result = []
    q = deque()

    #진입차수가 0인 것을 큐에 담기.
    for idx, item in enumerate(indegree):
        if not item:
            q.append(idx)

    while q:
        now = q.popleft()
        result.append()
        for data in graph[now]:
            indegree[data] -= 1
            if not indegree[data]:
                q.append(data)

    for i in result:
        print(i, end=" ")

topology_sort()