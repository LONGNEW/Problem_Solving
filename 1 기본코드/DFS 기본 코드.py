def DFS(graph, node, visit):
    visit[node] = True
    print(node, end=" ")

    for next_node in graph[node]:
        if not visit[next_node]:
            DFS(graph, next_node, visit)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [5, 6],
    [3, 4],
]
visit = [False] * 6
DFS(graph, 1, visit)