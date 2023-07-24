def solution(brown, yellow):
    # temp는 row가 가능한 범위의 가장 큰 값
    temp = int(yellow ** (1 / 2))
    for row in range(temp, 0, -1):
        if yellow % row != 0:
            continue

        col = yellow // row
        need_brown = row * 2 + col * 2 + 4
        # print(f"{[col + 2, row + 2]}, need_brown={need_brown}")
        if brown == need_brown:
            return [col + 2, row + 2]