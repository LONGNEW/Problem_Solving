from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = -float("inf")
        diff_ret = abs(ret - target)

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                diff_val = val - target

                if abs(diff_val) < diff_ret:
                    ret, diff_ret = val, abs(diff_val)

                if diff_val < 0:
                    j += 1
                else:
                    k -= 1

        return ret

s = Solution()
print(s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
print(s.threeSumClosest([1, 1, 1, 0], -100))
print(s.threeSumClosest([1, 1, 1, 0], 100))
print(s.threeSumClosest([-1,2,1,-4], 1))
print(s.threeSumClosest([0, 0, 0], 1))