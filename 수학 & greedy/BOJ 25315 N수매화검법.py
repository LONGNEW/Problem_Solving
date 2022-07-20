import sys

def CCW(x1, y1, x2, y2, x3, y3):
    ret = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    if ret == 0:
        return 0
    elif ret < 0:
        return -1
    elif ret > 0:
        return 1

def isIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    ab = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4)
    cd = CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2)

    if ab == 0 and cd == 0:
        if x1 + y1 > x2 + y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if x3 + y3 > x4 + y4:
            x3, y3, x4, y4 = x4, y4, x3, y3

        return x1 + y1 <= x4 + y4 and x3 + y3 <= x2 + y2

    return ab <= 0 and cd <= 0

n = int(sys.stdin.readline())
data = []

for i in range(n):
    x1, y1, x2, y2, w = map(int, sys.stdin.readline().split(" "))
    data.append((w, x1, y1, x2, y2))

data.sort()
ans = 0

for i in range(n):
    cnt = 1

    for j in range(i + 1, n):
        x1, y1, x2, y2 = data[i][1], data[i][2], data[i][3], data[i][4]
        x3, y3, x4, y4 = data[j][1], data[j][2], data[j][3], data[j][4]

        if isIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
            cnt += 1

    ans += data[i][0] * cnt

print(ans)
