def solution(numbers, hand):
    answer = ""
    keys = {
        "1":(0, 0), "2":(0, 1), "3":(0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2),
        "*": (3, 0), "0": (3, 1), "#": (3, 2),
    }

    left, right = "*", "#"
    for item in numbers:
        item = str(item)

        if item in ["1", "4", "7"]:
            answer += "L"
            left = item
        elif item in ["3", "6", "9"]:
            answer += "R"
            right = item
        else:
            x, y = keys[item]
            (xl, yl), (xr, yr) = keys[left], keys[right]
            l_dist = abs(xl - x) + abs(yl - y)
            r_dist = abs(xr - x) + abs(yr - y)
            if l_dist < r_dist:
                answer += "L"
                left = item
            elif l_dist > r_dist:
                answer += "R"
                right = item
            else:
                if hand == "right":
                    answer += "R"
                    right = item
                else:
                    answer += "L"
                    left = item

    return answer

print(solution([0, 0], "right"))
print(solution([1, 3, 4, 5,8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))