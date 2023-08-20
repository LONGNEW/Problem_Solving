from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n, i, maxReach, lastJump, jump = len(nums), 0, 0, 0, 0

        while lastJump < n - 1:
            maxReach = max(maxReach, i + nums[i])
            if i == lastJump:
                lastJump = maxReach
                jump += 1

            i += 1

        return jump