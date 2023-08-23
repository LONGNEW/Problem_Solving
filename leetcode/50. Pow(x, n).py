class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1

        if n < 0:
            x = 1 / x
            n = -n

        multiply = x
        while n != 0:
            if n % 2 == 1:
                ret *= multiply
            multiply *= multiply
            n = n >> 1

        return ret