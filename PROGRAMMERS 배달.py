from collections import deque

def solution(N, road, K):
    distance = [float("inf")] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    q = deque([1])
    distance[1] = 0
    while q:
        node = q.popleft()

        for next_node, weight in graph[node]:
            total = distance[node] + weight
            if total > K or total >= distance[next_node]:
                continue
            distance[next_node] = total
            q.append(next_node)

    cnt = 0
    for item in distance:
        if item != float("inf"):
            cnt += 1
    return cnt

print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))