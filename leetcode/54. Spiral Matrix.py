class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        col, row = len(matrix[0]), len(matrix)
        visit = [[0] * col for _ in range(row)]
        ret = []

        idx = 0
        x, y = 0, 0
        for _ in range(row * col):
            ret.append(matrix[x][y])
            visit[x][y] = 1
            x, y = x + dx[idx], y + dy[idx]

            if x < 0 or x >= row or y < 0 or y >= col or visit[x][y] == 1:
                x, y = x - dx[idx], y - dy[idx]
                idx += 1
                if idx == 4:
                    idx = 0
                x, y = x + dx[idx], y + dy[idx]
        return ret
