class Solution:
    def longestValidParentheses(self, s: str) -> int:
        unpair_idxes = []
        for i in range(len(s)):
            item = s[i]
            if item == ")":
                if unpair_idxes and s[unpair_idxes[-1]] == "(":
                        unpair_idxes.pop()
                        continue
            unpair_idxes.append(i)

        ret = 0
        prev = len(s)
        for item in unpair_idxes[::-1]:
            ret = max(ret, prev - 1 - item)
            prev = item
        ret = max(ret, prev)
        return ret

s = Solution()
print(s.longestValidParentheses("())"))
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses("()(()"))