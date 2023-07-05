class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        if not (s[0] in ["-", "+"] or 48 <= ord(s[0]) < 59):
            return 0

        ret = s[0]
        s = s[1:]
        while s and 48 <= ord(s[0]) < 59:
            ret += s[0]
            s = s[1:]

        try:
            ret = float(ret)
            ret = int(ret)
            ret = max(-2 ** 31, ret)
            ret = min(2 ** 31 - 1, ret)
        except:
            return 0

        return ret

s = Solution()
# print(s.myAtoi("  -0012a42"))
# print(s.myAtoi("3.14159"))
print(s.myAtoi("42"))
print(s.myAtoi("   -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("00000-42a1234"))