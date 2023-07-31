class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def recursive(remain, idx, ret):
            if remain < 0:
                return

            if remain == 0:
                answer.append(ret)
                return

            for idx in range(idx, len(candidates)):
                recursive(remain - candidates[idx], idx, ret + [candidates[idx]])
            return

        recursive(target, 0, [])
        return answer