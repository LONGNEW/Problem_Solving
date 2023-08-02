class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        nums.append(0)
        length = len(nums)

        for idx in range(length):
            if nums[idx] < 0 or nums[idx] >= length - 1:
                nums[idx] = 0

        for idx in range(length):
            # 해당 인덱스 값이 등장했는지는 원소의 나머지 값으로 계산.
            nums[nums[idx] % (length - 1)] += length - 1

        for idx in range(1, length):
            if nums[idx] // (length - 1) == 0:
                return idx
