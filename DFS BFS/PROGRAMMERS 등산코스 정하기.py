from collections import deque

def solution(n, paths, gates, summits):
    summits.sort()
    dict_sum = dict()
    dist, graph = [float("inf")] * (n + 1), [[] for _ in range(n + 1)]

    for item in summits:
        dict_sum[item] = 1

    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    q = deque([])
    for item in gates:
        q.append(item)
        dist[item] = 0

    while q:
        node = q.popleft()

        if node in dict_sum:
            continue

        for next_node, wei in graph[node]:
            temp_wei = max(dist[node], wei)
            if dist[next_node] <= temp_wei:
                continue
            dist[next_node] = temp_wei
            q.append(next_node)

    no, value = -1, float("inf")
    for item in summits:
        if value > dist[item]:
            no, value = item, dist[item]
    return [no, value]

# print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5]))
# print(solution(7,	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],	[1],	[2, 3, 4]	))
print(solution(7,	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7],	[1, 5]))
# print(solution(5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],	[1, 2],	[5]))
