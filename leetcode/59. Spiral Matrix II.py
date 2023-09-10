class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        idx = 0

        cnt = 1
        x, y = 0, 0
        ret = [[0] * n for _ in range(n)]

        for i in range(n * n):
            ret[x][y] = cnt
            cnt += 1

            nx, ny = x + dx[idx], y + dy[idx]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or ret[nx][ny] != 0:
                idx += 1
                if idx == 4: idx = 0

            x, y = x + dx[idx], y + dy[idx]

        return ret
