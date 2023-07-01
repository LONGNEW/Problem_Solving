class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), -1, -1):
            start = 0
            while start + i <= len(s):
                temp = s[start: start + i]
                rev_temp = temp[::-1]

                if temp == rev_temp:
                    return temp
                start += 1

# s = Solution()
# print(s.longestPalindrome("babad"))
# print(s.longestPalindrome("cbbd"))
