from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            idx = (left + right) // 2

            if nums[right] < nums[idx]:
                left = idx + 1
            else:
                right = idx

        idx_small = right
        idx_large = right - 1
        left, right = 0, len(nums) - 1
        if idx_small != 0:
            if nums[idx_small] <= target <= nums[right]:
                left = idx_small
            else:
                right = idx_large

        while left <= right:
            idx = (left + right) // 2
            if target < nums[idx]:
                right = idx - 1
            else:
                left = idx + 1

        if nums[right] != target:
            return -1
        return right

s = Solution()
print(s.search([1, 3], 2))
print(s.search([1, 3], 1))
print(s.search([1], 0))
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([1], 2))
print(s.search([4,5,6,7,0,1,2], 0))