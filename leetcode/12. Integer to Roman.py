class Solution:
    def intToRoman(self, num: int) -> str:
        ret = ""
        temp = {
            "I" : 1, "IV" : 4,
            "V" : 5, "IX" : 9,
            "X" : 10, "XL" : 40,
            "L" : 50, "XC" : 90,
            "C" : 100, "CD" : 400,
            "D" : 500, "CM" : 900,
            "M" : 1000,
        }

        keys = list(temp.keys())[::-1]
        for item in keys:
            divide = num // temp[item]
            ret += item * divide
            num %= temp[item]

        return ret

# s = Solution()
# print(s.intToRoman(3))
# print(s.intToRoman(58))
# print(s.intToRoman(1994))