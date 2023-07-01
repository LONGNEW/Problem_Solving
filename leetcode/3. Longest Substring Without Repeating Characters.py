class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = dict()
        start = 0

        ret = 0
        for end in range(len(s)):
            item = s[end]
            if item not in alpha:
                alpha[item] = 0

            if alpha[item] == 1:
                while alpha[item] != 0:
                    alpha[s[start]] -= 1
                    start += 1

            alpha[item] += 1
            ret = max(ret, end - start + 1)

        return ret
#
# s = Solution()
# print(s.lengthOfLongestSubstring("abcabcbb"))
# print(s.lengthOfLongestSubstring("bbbbb"))
# print(s.lengthOfLongestSubstring("pwwkew"))
# print(s.lengthOfLongestSubstring(""))
# print(s.lengthOfLongestSubstring(" "))