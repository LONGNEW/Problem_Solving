import sys

R, C = map(int, sys.stdin.readline().split())
graph = [[] for i in range(R)]
alpha = [0] * (26)
ans = 0

for i in range(R):
    data = sys.stdin.readline().strip()
    for j in range(len(data)):
        graph[i].append(ord(data[j]) - 65)

def DFS(x, y, cnt):
    global ans

    ans = max(ans, cnt)
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= R or nx < 0 or ny < 0 or ny >= C:
            continue

        if not alpha[graph[nx][ny]]:
            alpha[graph[nx][ny]] += 1
            DFS(nx, ny, cnt + 1)
            alpha[graph[nx][ny]] -= 1

alpha[graph[0][0]] = 1
DFS(0, 0, 1)

print(ans)