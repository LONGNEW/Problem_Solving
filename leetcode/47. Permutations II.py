class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        global ret
        ret = dict()

        def recursive(used, ordered):
            if len(ordered) == len(nums):
                ret[tuple(ordered)] = 1
                return

            for key in used.keys():
                if used[key] <= 0:
                    continue

                used[key] -= 1
                recursive(used, ordered + [key])
                used[key] += 1

        used = {item: 0 for item in nums}
        for item in nums:
            used[item] += 1

        recursive(used, [])
        return ret