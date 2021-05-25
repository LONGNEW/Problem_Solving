import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
degree = [0] * (n + 1)
data = [0] * (n + 1)
ans = [0] * (n + 1)
q = deque()

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))

    data[i + 1] = temp[0]

    # 본인에게 들어오는 간선이 없음. 위상정렬의 시작점
    if len(temp) == 2:
        q.append(i + 1)
        ans[i + 1] = temp[0]
        continue

    # temp 값에 들어있는 Node에서 i + 1번 노드로 들어오는 간선을 입력받는 것.
    for j in range(1, len(temp) - 1):
        # start = temp[j]
        graph[temp[j]].append(i + 1)
        degree[i + 1] += 1

while q:
    now = q.popleft()

    for next_node in graph[now]:
        degree[next_node] -= 1
        ans[next_node] = max(ans[next_node], data[next_node] + ans[now])

        if degree[next_node] == 0:
            q.append(next_node)

for i in range(1, n + 1):
    print(ans[i])














