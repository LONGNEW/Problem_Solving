import sys
import math

data = list(map(int, sys.stdin.readline().split()))

def getDistance(x1, y1, x2, y2):
    return math.sqrt( math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) )

aX1 = data[0]
aY1 = data[1]
aX2 = data[2]
aY2 = data[3]
cX1 = data[4]
cY1 = data[5]
cX2 = data[6]
cY2 = data[7]

interval = 1000000

aDX = (aX2 - aX1) / interval
aDY = (aY2 - aY1) / interval
cDX = (cX2 - cX1) / interval
cDY = (cY2 - cY1) / interval
try:
    i = -1 * ( (aX1 - cX1) * (aDX - cDX) + (aY1 - cY1) * (aDY - cDY) ) / ( math.pow(aDX - cDX, 2) + math.pow(aDY - cDY, 2) )
    ret = getDistance(aX1 + aDX * i, aY1 + aDY * i, cX1 + cDX * i, cY1 + cDY * i)
    if 0 < i < interval:
        print(ret)
    else:
        a = getDistance(aX1, aY1, cX1, cY1)
        b = getDistance(aX2, aY2, cX2, cY2)
        print(min(a, b))
except ZeroDivisionError:
    a = getDistance(aX1, aY1, cX1, cY1)
    b = getDistance(aX2, aY2, cX2, cY2)
    print(min(a, b))