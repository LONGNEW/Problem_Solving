def solution(prices):
    answer = [0] * len(prices)
    temp = []

    for idx, item in enumerate(prices):
        while temp:
            top_idx, top_value = temp[-1]

            if top_value <= item:
                break
            if top_value > item:
                temp.pop()
                answer[top_idx] = idx - top_idx
        temp.append((idx, item))

    while temp:
        temp_idx, temp_item = temp.pop()
        answer[temp_idx] = len(prices) - temp_idx - 1
    return answer

print(solution([1, 2, 3, 2, 3]))