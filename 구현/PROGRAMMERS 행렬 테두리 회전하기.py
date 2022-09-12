def solution(rows, cols, queries):
    answer, cnt = [], 1
    rows, cols = rows + 1, cols + 1
    data = [[0] * cols for _ in range(rows)]
    for i in range(1, rows):
        for j in range(1, cols):
            data[i][j] = cnt
            cnt += 1

    for x1, y1, x2, y2 in queries:
        temp = [[0] * cols for _ in range(rows)]

        def dfs(x, y, min_val):
            if x == x1 and y != y2:
                dx, dy = x, y + 1
            elif x != x2 and y == y2:
                dx, dy = x + 1, y
            elif x == x2 and y != y1:
                dx, dy = x, y - 1
            else:
                dx, dy = x - 1, y

            if temp[dx][dy] != 0:
                return min_val

            temp[dx][dy] = data[x][y]
            return dfs(dx, dy, min(min_val, data[x][y]))

        min_val = dfs(x1, y1, float("inf"))


        answer.append(min_val)
        for i in range(1, rows):
            for j in range(1, cols):
                if temp[i][j]:
                    data[i][j] = temp[i][j]

    return answer

print(solution(6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,	3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))