class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = list(s), list(p)
        dp = dict()

        def recursive(i, j):
            if j == len(p):
                return i == len(s)
            if (i, j) in dp:
                return dp[(i, j)]

            # i == len(s)인 시점부터 matched는 false로 고정
            # 이걸 유지해서 밑에서 matched들이 먼저 false라 i를 키우는 재귀는 돌지 않음.
            # 그래서 23번째 줄의 j + 2 하는 재귀만 수행해서 답을 낸다.
            matched = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                # matched의 경우 현재 "*"에 s의 문자를 걸리게 하고 넘어감.
                matched = matched and recursive(i + 1, j)

                # 아래의 recursive는 지금 "*"을 무시하고 현재 i를 유지하게 함.
                # 경우의 수가 2가지로 나뉘는 것을 모두 경험함.
                ret = recursive(i, j + 2) or matched
            else:
                ret = matched and recursive(i + 1, j + 1)
            dp[(i, j)] = ret
            return dp[(i, j)]

        return recursive(0, 0)

    # def isMatch(self, s: str, p: str) -> bool:
    #     s, p = list(s), list(p)
    #     len_s, len_p = len(s), len(p)
    #     dp = [[0] * (len_s + 1) for _ in range(len_p + 1)]
    #
    #     dp[0][0] = 1
    #     for j in range(1, len_p + 1):
    #         cha_p = p[j - 1]
    #         if cha_p == "*":
    #             dp[j][0] = dp[j - 2][0]
    #
    #     for i in range(1, len_p + 1):
    #         for j in range(1, len_s + 1):
    #             cha_p, cha_s = p[i - 1], s[j - 1]
    #
    #             if cha_p == "*":
    #                 prev_p = p[i - 2]
    #                 dp[i][j] = dp[i - 2][j] or ((cha_s == prev_p or prev_p == ".") and dp[i][j - 1])
    #             else:
    #                 dp[i][j] = dp[i - 1][j - 1] and (cha_s == cha_p or cha_p == ".")
    #
    #
    #     return dp[-1][-1] == 1

sol = Solution()
print(sol.isMatch("aa", "a"))
