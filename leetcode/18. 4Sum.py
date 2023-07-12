from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = dict()
        def recursive(i, l):
            if i + 2 >= l:
                return set()
            if (i, l) in dp:
                return dp[(i, l)]

            result = set()
            j, k = i + 1, l - 1
            while j < k:
                val = nums[i] + nums[k] + nums[l] + nums[j]
                if val == target:
                    result.add((nums[i], nums[j], nums[k], nums[l]))
                    j += 1
                    k -= 1
                elif val > target:
                    k -= 1
                else:
                    j += 1

            dp[(i + 1, l)] = recursive(i + 1, l)
            result.update(dp[(i + 1, l)])

            dp[(i, l - 1)] = recursive(i, l - 1)
            result.update(dp[(i, l - 1)])

            dp[(i, l)] = result
            return result

        nums.sort()
        ret = recursive(0, len(nums) - 1)
        return list(ret)


# s = Solution()
# print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
# print(s.fourSum([2, 2, 2, 2, 2], 8))
