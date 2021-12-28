import sys

def dfs(node):
    if visit[node]:
        return False

    visit[node] = 1

    for next_node in food[node]:
        prev = ans[next_node]
        if prev == -1:
            ans[next_node] = node
            return True

        if dfs(prev):
            ans[next_node] = node
            return True

    return False

n = int(sys.stdin.readline())
graph, ans, food = [], [-1] * n, dict()

for i in range(n):
    size, speed, brain = map(int, sys.stdin.readline().split())
    graph.append((size, speed, brain))
    food[i] = []

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if graph[i][0] == graph[j][0] and graph[i][1] == graph[j][1] and graph[i][2] == graph[j][2] and i > j:
            continue

        if graph[i][0] >= graph[j][0] and graph[i][1] >= graph[j][1] and graph[i][2] >= graph[j][2]:
            food[i].append(j)

for i in range(2):
    for j in range(n):
        visit = [0] * n
        dfs(j)

print(ans.count(-1))