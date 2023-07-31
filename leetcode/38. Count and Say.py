class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return f"1"

        ret = ""
        temp = self.countAndSay(n - 1)
        prev, cnt = "", 0
        for item in temp:
            if prev != item and cnt > 0:
                ret += f"{cnt}{prev}"
                cnt = 0

            prev = item
            cnt += 1

        ret += f"{cnt}{prev}"
        return ret