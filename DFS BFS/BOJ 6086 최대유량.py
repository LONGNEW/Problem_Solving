import sys
from collections import deque

def bfs():
    visit = dict()
    for key in graph.keys():
        visit[key] = 0

    visit["A"] = 1
    q = deque(["A"])

    while q:
        node = q.popleft()

        if node == "Z":
            return True

        for next_node in graph[node]:
            if not visit[next_node] and value[node][next_node] > 0:
                visit[next_node] = 1
                prev[next_node] = node
                q.append(next_node)

    return False

def ford():
    ret = 0

    while bfs():
        min_flow, temp = float('inf'), "Z"
        while temp != "A":
            min_flow = min(min_flow, value[prev[temp]][temp])
            temp = prev[temp]

        temp = "Z"
        while temp != "A":
            value[prev[temp]][temp] -= min_flow
            value[temp][prev[temp]] += min_flow
            temp = prev[temp]

        ret += min_flow
    return ret

n = int(sys.stdin.readline())
graph, value, prev = dict(), dict(), dict()

for _ in range(n):
    a, b, c = sys.stdin.readline().split()
    c = int(c)

    if a not in value:
        graph[a] = []
        value[a] = dict()

    if b not in value:
        graph[b] = []
        value[b] = dict()

    graph[a].append(b)
    graph[b].append(a)

    if a not in value[b]:
        value[b][a] = 0
    if b not in value[a]:
        value[a][b] = 0

    value[b][a] += c
    value[a][b] += c

print(ford())