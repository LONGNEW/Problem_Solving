def solution(plans):
    answer = []
    stack = []

    for i in range(len(plans)):
        time = plans[i][1]
        h, m = time.split(":")
        plans[i][1] = int(h) * 60 + int(m)
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x: x[1])
    for name, start, play in plans:
        if stack:
            _, c_start, _ = stack[-1]
            remain = start - c_start

            while remain > 0 and stack:
                c_name, c_start, c_play = stack.pop()
                if remain >= c_play:
                    remain -= c_play
                    answer.append(c_name)
                else:
                    stack.append((c_name, c_start, c_play - remain))
                    break
        stack.append((name, start, play))

    for i in range(len(stack) - 1, -1, -1):
        answer.append(stack[i][0])
    return answer

print(solution([["A", "11:50", "30"], ["B", "13:00", "20"], ["C", "13:10", "30"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "15:00", "30"], ["computer", "12:30", "100"]]))