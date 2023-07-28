class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]

            if val <= target:
                l = mid + 1
            else:
                r = mid - 1
        temp_l, temp_r = l, r

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]

            if val >= target:
                r = mid - 1
            else:
                l = mid + 1

        if temp_r < l:
            return [-1, -1]
        return [l, temp_r]
