from _collections import deque

def BFS(graph, start, visit):
    #동작과정1 : 탐색 시작 노드를 큐에 삽입 하고 방문 처리.
    q = deque([start])
    visit[start] = True

    while q:
        # 2. 큐에서 노드를 꺼내 
        node = q.popleft()
        print(node, end=" ")
        for next_node in graph[node]:
            # 2. 방문 하지 않은 노드를 방문 처리 하고 큐에 추가.
            if not visit[next_node]:
                q.append(next_node)
                visit[next_node] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [5, 6],
    [3, 4],
]
visit = [False] * 6
BFS(graph, 1, visit)