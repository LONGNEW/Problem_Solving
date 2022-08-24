def solution(survey, choices):
    answer = ''
    data = dict()

    for item in ["R", "T", "C", "F", "J", "M", "A", "N"]:
        data[item] = 0

    for i in range(len(survey)):
        left, right = survey[i][0], survey[i][1]
        value = 4 - choices[i]

        if value > 0:
            data[left] += abs(value)
        else:
            data[right] += abs(value)

    if data["R"] >= data["T"]:
        answer += "R"
    else:
        answer += "T"

    if data["C"] >= data["F"]:
        answer += "C"
    else:
        answer += "F"

    if data["J"] >= data["M"]:
        answer += "J"
    else:
        answer += "M"

    if data["A"] >= data["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))