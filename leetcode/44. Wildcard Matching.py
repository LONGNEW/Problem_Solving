class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length_s, length_p = len(s), len(p)
        dp = [[0] * (length_s + 1) for _ in range(length_p + 1)]

        dp[0][0] = 1
        for i in range(1, length_p + 1):
            if p[i - 1] != "*":
                break
            dp[i][0] = 1

        for p_idx in range(1, length_p + 1):
            for s_idx in range(1, length_s + 1):
                p_val, s_val = p[p_idx - 1], s[s_idx - 1]
                dp[p_idx][s_idx] = 0
                if p_val == s_val or p_val == "?":
                    dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1]
                    continue
                if p_val == "*":
                    dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1] or dp[p_idx][s_idx - 1]
        return dp[-1][-1]