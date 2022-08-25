def solution(info, edges):
    graph = [[] for _ in range(len(info))]

    def dfs(node, sheep, wolf, not_visit):
        sheep += 1 if not info[node] else 0
        wolf += info[node]
        if sheep <= wolf:
            return sheep

        ans = 0
        for next_node in range(len(not_visit)):
            if not not_visit[next_node]:
                continue

            temp = [i for i in not_visit]
            temp[next_node] = 0
            for idx in graph[next_node]:
                temp[idx] = 1
            ans = max(ans, dfs(next_node, sheep, wolf, temp))

        return max(sheep, ans)

    for a, b in edges:
        graph[a].append(b)

    not_visit = [0] * len(info)
    for idx in graph[0]:
        not_visit[idx] = 1

    return dfs(0, 0, 0, not_visit)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0],	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))