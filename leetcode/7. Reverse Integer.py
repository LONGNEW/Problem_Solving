class Solution:
    def reverse(self, x: int) -> int:
        ret = ""
        if x == 0:
            return x

        if x < 0:
            ret += "-"
            x *= -1

        while x > 0:
            ret += str(x % 10)
            x //= 10

        ret = int(ret)
        if ret < -2 ** 31 or ret > 2 ** 31 - 1:
            return 0
        return ret

# s = Solution()
# print(s.reverse(1534236469))
# print(s.reverse(-123))
# print(s.reverse(120))