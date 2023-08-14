class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        length2 = len(num2)
        dp = [0] * (len(num1) * 2)
        temp_idx = len(dp)
        for i in range(length2 - 1, -1, -1):
            temp_idx -= 1
            for j in range(len(num1) - 1, -1, -1):
                value = int(num1[j]) * int(num2[i])

                idx = temp_idx - (len(num1) - 1 - j)
                temp_sum = value + dp[idx]
                carry = temp_sum // 10
                dp[idx] = temp_sum % 10
                idx -= 1

                while carry:
                    dp[idx] += carry
                    carry = dp[idx] // 10
                    dp[idx] = dp[idx] % 10
                    idx -= 1

        if dp[0] == 0:
            dp = dp[1:]

        ret = ""
        for item in dp:
            ret += f"{item}"
        return ret


s = Solution()
print(s.multiply("9", "99"))
print(s.multiply("123", "456"))