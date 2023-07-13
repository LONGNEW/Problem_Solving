from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def recursive(l, r, string):
            if l == 0 and r == 0:
                return ret.append(string)
            if l > r:
                return

            if l > 0:
                recursive(l - 1, r, string + "(")
            if r > 0:
                recursive(l, r - 1, string + ")")
        recursive(n, n, "")
        return ret