def solution(s):
    answer = float("inf")
    length = len(s)
    if length == 1:
        return 1

    for i in range(1, length // 2 + 1):
        temp = ""

        idx = 0
        while idx < length:
            if idx + i >= length:
                break

            # target이 길이만큼 생기는지 확인 필요.
            target, cnt, space = s[idx:idx + i], 1, ""
            idx += i
            while idx + i <= length and target == s[idx:idx + i]:
                cnt += 1
                idx += i
            temp += f"{space if cnt == 1 else cnt}{target}"
        temp += f"{s[idx:length]}"
        answer = min(answer, len(temp))

    return answer

print(solution("a"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))