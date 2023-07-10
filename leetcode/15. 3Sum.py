from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            if j >= k:
                continue

            while j < k:
                val1, val2, val3 = nums[i], nums[j], nums[k]
                temp = val1 + val2 + val3
                if temp == 0:
                    ret.add((val1, val2, val3))
                    j += 1
                    k -= 1
                    continue

                if temp > 0:
                    k -= 1
                else:
                    j += 1

        return list(ret)

# s = Solution()
# print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
# print(s.threeSum([-1,0,1,2,-1,-4]))
# print(s.threeSum([0,1,1]))
# print(s.threeSum([0,0,0]))