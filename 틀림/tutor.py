def solution(table, languages, preference):
    temp, ans = dict(), []

    for i in range(len(table)):
        text = table[i].split()
        pos, value = text[0], [0] * (len(languages))

        for j in range(1, len(text)):
            if text[j] not in languages:
                continue
            idx = languages.index(text[j])
            value[idx] = len(text) - j

        temp[pos] = value

    for item in temp.keys():
        now = temp[item]
        for i in range(len(now)):
            now[i] = now[i] * preference[i]
        ans.append((sum(now), item))

    ans.sort(key=lambda x:(-x[0], x[1]))
    return ans[0][1]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

print(solution(table, languages, preference))