from collections import deque


def solution(n, s, a, b, fares):
    answer = float("inf")

    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    # 모든 위치에 대해 합승을 해서 도착했다고 가정
    # 거기서 부터 A, B로 가기.
    for node in range(1, n + 1):
        distance = [float("inf")] * (n + 1)
        q = deque([(node, 0)])
        distance[node] = 0
        while q:
            now_node, dist = q.popleft()

            if distance[now_node] < dist:
                continue

            for next_node, weight in graph[now_node]:
                total_fare = distance[now_node] + weight
                if total_fare >= distance[next_node]:
                    continue
                distance[next_node] = total_fare
                q.append((next_node, total_fare))
        answer = min(answer, distance[a] + distance[b] + distance[s])
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))