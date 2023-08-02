class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def recursive(used, idx, sum):
            if sum > target:
                return
            if sum == target:
                ret.append(used)
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    # 맨 처음 등장하는 i의 경우에는 언제나 재귀를 수행해줌.
                    # 그러나 그 이후에는 해당 값을 다시 확인하지 않기 위해.
                    # [1, 2, 2, 2]
                    # 0, 1, 2의 idx를 확인 하면 되지.
                    # 0, 1, 3의 경우는 안 해도 되니까 이를 판단하기 위한 조건임.
                    continue

                item = candidates[i]
                recursive(used + [item], i + 1, sum + item)

        recursive([], 0, 0)

        return ret