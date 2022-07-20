import sys

def CCW(x1, y1, x2, y2, x3, y3):

    ret = ((x2 - x1) * (y3 - y1)) - ((y2 - y1) * (x3 - x1))
    if ret == 0:
        return 0
    elif ret < 0:
        return -1
    elif ret > 0:
        return 1

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().split(" "))

res = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4)
print(1 if res == -1 else 0)