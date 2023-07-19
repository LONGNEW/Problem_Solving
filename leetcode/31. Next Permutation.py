from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = None
        for i in range(len(nums) - 1, 0, -1):
            prev, now = nums[i - 1], nums[i]
            if prev < now:
                k = i - 1
                break

        if k is None:
            nums.sort()
            return

        l = None
        for i in range(len(nums) - 1, 0, -1):
            target, now = nums[k], nums[i]
            if target < now:
                l = i
                break

        nums[k], nums[l] = nums[l], nums[k]
        temp = nums[k + 1:][::-1]
        for i in range(k + 1, len(nums)):
            nums[i] = temp[i - (k + 1)]

s = Solution()
print(s.nextPermutation([1, 3, 2]))
print(s.nextPermutation([1, 2]))
print(s.nextPermutation([3, 2, 1]))
print(s.nextPermutation([1, 2, 3]))