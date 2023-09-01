class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag = False
        can_move = 0
        length = len(nums)

        for idx, step in enumerate(nums):
            if idx > can_move:
                break

            if idx + step >= length:
                flag = True
                break

            can_move = max(idx + step, can_move)

        if can_move == length - 1:
            return True
        return flag


