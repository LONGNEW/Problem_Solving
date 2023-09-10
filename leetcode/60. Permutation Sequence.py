class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        can_use = dict()
        for i in range(1, n + 1):
            can_use[i] = 1

        cnt_permutation = 1
        biggest_idx = n - 1
        for i in range(1, n):
            cnt_permutation *= i

        ret = ""
        while k != 0:

            for key in can_use.keys():
                if can_use[key] == 0:
                    continue

                if k <= cnt_permutation:
                    ret += f"{key}"
                    can_use[key] = 0
                    break
                k -= cnt_permutation

            if biggest_idx == 0:
                break

            cnt_permutation = cnt_permutation // biggest_idx
            biggest_idx -= 1
        return ret

s = Solution()
print(s.getPermutation(3, 3))