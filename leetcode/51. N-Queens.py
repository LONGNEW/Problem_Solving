from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        dx = [-1, -1, -1]
        dy = [0, 1, -1]

        def valid(queens, x, y):
            for i in range(3):
                nx, ny = x + dx[i], y + dy[i]
                while 0 <= nx < n and 0 <= ny < n:
                    if ny == queens[nx]:
                        return False
                    nx, ny = nx + dx[i], ny + dy[i]
            return True

        def recursive(queens, idx):
            if idx == n:
                temp_ret = []
                for i in range(n):
                    temp = ["."] * n
                    ny = queens[i]
                    temp[ny] = "Q"
                    temp_ret.append("".join(temp))
                ret.append(temp_ret)
                return

            for i in range(n):
                if valid(queens, idx, i):
                    queens[idx] = i
                    recursive(queens, idx + 1)
                    queens[idx] = -1

        recursive([-1] * n, 0)
        return ret


s = Solution()
print(s.solveNQueens(4))