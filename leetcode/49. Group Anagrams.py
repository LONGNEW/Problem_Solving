class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = dict()

        # use key as a sorted chars
        # use value as a element of strs array
        for item in strs:
            words = [c for c in item]
            words.sort()
            words = tuple(words)

            if words not in ret:
                ret[words] = []
            ret[words].append(item)

        ans = []
        for key in ret.keys():
            ans.append(ret[key])
        return ans