class Solution:
    def medianValue(self, arr1, arr2, targetIdx):
        if not arr1: return arr2[targetIdx]
        if not arr2: return arr1[targetIdx]

        idxA, idxB = len(arr1) // 2, len(arr2) // 2
        valA, valB = arr1[idxA], arr2[idxB]

        # need to fix that valA is always the small one.
        if valA > valB:
            valA, valB = valB, valA
            idxA, idxB = idxB, idxA
            arr1, arr2 = arr2, arr1

        # if idx is 3 then 3 of element is in front of that one.
        cntMaxSmall = idxA + idxB

        if targetIdx <= cntMaxSmall:
            # valB can not be ignored
            return self.medianValue(arr1, arr2[:idxB], targetIdx)
        else:
            # valA can be ignored
            return self.medianValue(arr1[idxA + 1:], arr2, targetIdx - idxA - 1)

    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        targetIdx = length // 2

        val1 = self.medianValue(nums1, nums2, targetIdx)
        if length % 2 == 0:
            val2 = self.medianValue(nums1, nums2, targetIdx - 1)
            return (val1 + val2) / 2

        return val1

sol = Solution()
print(Solution.findMedianSortedArrays(sol, [1, 3], [2]))
print(Solution.findMedianSortedArrays(sol, [1, 2], [3, 4]))