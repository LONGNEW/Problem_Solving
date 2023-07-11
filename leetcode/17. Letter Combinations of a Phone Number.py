from typing import List
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        data = {        2:"abc", 3:"def",
                4:"ghi", 5:"jkl", 6:"mno",
                7:"pqrs", 8:"tuv", 9:"wxyz"}

        target_len = len(digits)
        if target_len == 0:
            return ret

        q = deque([("", 0)])
        while q:
            cha, next_idx = q.popleft()

            digit = int(digits[next_idx])
            next_idx += 1
            for next_cha in data[digit]:
                temp_cha = cha
                temp_cha += next_cha

                if next_idx == target_len:
                    ret.append(temp_cha)
                    continue
                q.append((temp_cha, next_idx))
        return ret

s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))