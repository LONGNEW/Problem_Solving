from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    length = len(q1) + len(q2)
    q1_sum, q2_sum = sum(q1), sum(q2)
    answer = 0

    total = q1_sum + q2_sum
    if total % 2 == 1:
        return -1

    if max(max(q1), max(q2)) > total // 2:
        return -1

    while q1_sum != (total // 2):
        if answer > length * 2:
            return -1

        answer += 1
        if q1_sum > q2_sum:
            popped_item = q1.popleft()
            q2.append(popped_item)
            q1_sum -= popped_item
            q2_sum += popped_item
        else:
            popped_item = q2.popleft()
            q1.append(popped_item)
            q1_sum += popped_item
            q2_sum -= popped_item
    return answer
