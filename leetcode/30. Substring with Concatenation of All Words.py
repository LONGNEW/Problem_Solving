from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        word_len = len(words[0])
        word_cnt = len(words)

        data, temp_data = dict(), dict()
        for item in words:
            temp_data[item] = 0
            if item not in data:
                data[item] = 1
            else:
                data[item] += 1

        for idx in range(word_len):
            start, end = idx, idx + word_len
            temp_cnt = 0

            for key in temp_data.keys():
                temp_data[key] = 0

            while end <= len(s):
                temp_word = s[end - word_len:end]
                if start + word_len > len(s):
                    break

                if temp_word not in data:
                    while start < end:
                        remove_word = s[start:start + word_len]
                        if remove_word in temp_data:
                            temp_data[remove_word] -= 1
                            temp_cnt -= 1
                        start += word_len
                    end += word_len
                    continue

                while temp_data[temp_word] >= data[temp_word]:
                    remove_word = s[start:start + word_len]
                    if remove_word in temp_data:
                        temp_data[remove_word] -= 1
                        temp_cnt -= 1
                    start += word_len

                temp_data[temp_word] += 1
                temp_cnt += 1
                end += word_len

                if temp_cnt == word_cnt:
                    ret.append(start)

        return ret

s = Solution()
print(s.findSubstring("aaaaaaaaaaaaaa", ["aa","aa"]))
print(s.findSubstring("a", ["a"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))