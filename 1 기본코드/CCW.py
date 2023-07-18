def CCW(x1, y1, x2, y2, x3, y3):
    # a (x1, y1) | b (x2, y2)
    # c (x3, y3)
    # ab 를 기준으로 c의 방향성을 찾음.
    # need three coordinate in argument.
    ret = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    if ret == 0:
        # 평행한 경우
        return 0
    elif ret < 0:
        # 시계 방향
        return -1
    elif ret > 0:
        # 반시계 방향
        return 1

def isIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # a (x1, y1) | b (x2, y2)
    # c (x3, y3) | d (x4, y4)
    ab = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4)
    cd = CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2)

    if (ab == 0 and cd == 0):
        if x1 + y1 > x2 + y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if x3 + y3 > x4 + y4:
            x3, y3, x4, y4 = x4, y4, x3, y3

        return x1 + y1 <= x4 + y4 and x3 + y3 <= x2 + y2

    return ab <= 0 and cd <= 0