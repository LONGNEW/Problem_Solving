from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check_valid(x, y, target):
            # row check
            for i in range(9):
                value = board[x][i]
                if value == target:
                    return False

            # col check
            for i in range(9):
                value = board[i][y]
                if value == target:
                    return False

            start_x = (x // 3) * 3
            start_y = (y // 3) * 3
            for dx in range(3):
                for dy in range(3):
                    value = board[start_x + dx][start_y + dy]
                    if value == target:
                        return False
            return True

        def vacant():
            for x in range(9):
                for y in range(9):
                    if board[x][y] == ".":
                        return x, y
            return -1, -1
        def recursive():
            x, y = vacant()
            if x == -1 and y == -1:
                return True

            for item in range(1, 10):
                if check_valid(x, y, f"{item}"):
                    board[x][y] = f"{item}"
                    if recursive():
                        return True
                board[x][y] = "."

        recursive()

s = Solution()
print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))