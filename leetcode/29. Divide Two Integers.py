class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ret = dividend / divisor
        if ret < -2 ** 31:
            return -2 ** 31
        if ret > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return int(ret)