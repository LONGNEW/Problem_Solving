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


# from collections import deque
#
#
# def solution(n, paths, gates, summits):
#     summits.sort()
#
#     # 초기에 산봉우리 초기화, 그래프 생성
#     # summits에는 최솟값을 저장함.
#     summits = {i: float("inf") for i in summits}
#     graph = [[] for _ in range(n + 1)]
#     for i, j, w in paths:
#         graph[i].append((j, w))
#         graph[j].append((i, w))
#
#     # intensity : visit과 같은 역할을 하도록 (강도가 제일 작은 걸 통해서 BFS 수행)
#     intensity = {i: float("inf") for i in range(n + 1)}
#     q = deque(gates)
#     for item in gates:
#         intensity[item] = 0
#
#     # BFS : 현재 inten < 다음 inten 인 경우에 Q에 넣고 게속 돌기
#     while q:
#         node = q.popleft()
#         inten = intensity[node]
#
#         if node in summits:
#             summits[node] = inten if inten < summits[node] else summits[node]
#             continue
#
#         for next_node, weight in graph[node]:
#             compare_inten = max(inten, weight)
#             if compare_inten >= intensity[next_node]:
#                 continue
#             intensity[next_node] = compare_inten
#             q.append(next_node)
#
#     # 결과 출력하기.
#     inten, num = float("inf"), -1
#     for key in summits.keys():
#         if inten > summits[key]:
#             inten, num = summits[key], key
#     return [num, inten]
#
# print(solution(6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5]))