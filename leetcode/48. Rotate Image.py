class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        temp_matrix = [[-1] * n for _ in range(n)]

        # matrix[0][~], matrix[1][~]
        # =>
        # matrix[~][n - 1], matrix[~][n - 2]

        for x in range(n):
            for y in range(n):
                value = matrix[x][y]
                temp_matrix[y][n - 1 - x] = value

        for x in range(n):
            for y in range(n):
                matrix[x][y] = temp_matrix[x][y]