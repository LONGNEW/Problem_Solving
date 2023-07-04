class Solution:
    def convert(self, s: str, numRows: int) -> str:
        diff = (numRows - 1) * 2
        if diff == 0:
            diff = 1

        ret = ""
        for i in range(numRows):
            for idx in range(i, len(s), diff):
                ret += s[idx]
                if i != 0 and i != numRows - 1:
                    step1 = (numRows - 1 - i) * 2
                    if idx + step1 >= len(s):
                        continue
                    ret += s[idx + step1]
        return ret

    # def convert(self, s: str, numRows: int) -> str:
    #     numCols = len(s) // numRows
    #     numCols += (numCols - 1) * (numRows // 2)
    #
    #     temp = [[""] * numCols for _ in range(numRows)]
    #     dx, dy = {False: 1, True: -1}, {False: 0, True: 1}
    #
    #     x, y = 0, 0
    #     flag = True
    #     for item in s:
    #         temp[x][y] = item
    #
    #         if x == 0 or x == numRows - 1:
    #             flag = not flag
    #         x, y = x + dx[flag], y + dy[flag]
    #
    #     ret = ""
    #     for item in temp:
    #         for cha in item:
    #             ret += cha
    #     return ret

# s = Solution()
# print(s.convert("PAYPALISHIRING", 3))
# print(s.convert("PAYPALISHIRING", 4))
# print(s.convert("A", 1))