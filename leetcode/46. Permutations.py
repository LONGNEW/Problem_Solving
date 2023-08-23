class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        global ret
        ret = []

        def recursive(used, ordered):
            if len(ordered) == len(nums):
                ret.append(ordered)
                return

            for key in used.keys():
                if used[key] == 1:
                    continue

                used[key] = 1
                recursive(used, ordered + [key])
                used[key] = 0

        used = {item: 0 for item in nums}
        recursive(used, [])
        return ret
