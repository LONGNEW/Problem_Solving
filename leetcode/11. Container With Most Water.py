from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        ret = 0

        while low < high:
            val_l, val_h = height[low], height[high]
            val = min(val_l, val_h)
            ret = max(ret, (high - low) * val)

            if val_l > val_h:
                high -= 1
            else:
                low += 1

        return ret

#
# s = Solution()
# print(s.maxArea([1,3,2,5,25,24,5]))
# print(s.maxArea([1,8,100,2,100,4,8,3,7]))
# print(s.maxArea([1,8,6,2,5,4,8,3,7]))
# print(s.maxArea([1,1]))
# print(s.maxArea([1,1, 1,5,5,1,1]))