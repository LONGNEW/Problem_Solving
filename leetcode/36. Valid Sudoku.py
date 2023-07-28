class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            temp = {j: 0 for j in range(1, 10)}
            data = board[row]

            for item in data:
                if item == ".":
                    continue

                val = int(item)
                if temp[val] != 0:
                    return False
                temp[val] += 1

        for col in range(len(board)):
            temp = {j: 0 for j in range(1, 10)}

            for row in range(len(board)):
                item = board[row][col]
                if item == ".":
                    continue

                val = int(item)
                if temp[val] != 0:
                    return False
                temp[val] += 1

        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                used = {j: 0 for j in range(1, 10)}

                for dx in range(3):
                    for dy in range(3):
                        item = board[x + dx][y + dy]
                        if item == ".":
                            continue

                        val = int(item)
                        if used[val] != 0:
                            return False
                        used[val] += 1

        return True
