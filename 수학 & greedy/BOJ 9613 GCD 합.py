import sys
from math import gcd

t = int(sys.stdin.readline())
for i in range(t):
    num = list(map(int, sys.stdin.readline().split()))
    ans = 0

    for j in range(1, num[0]):
        for k in range(j + 1, num[0] + 1):
            ans += gcd(num[j], num[k])
    print(ans)

--------------------------------------------------------------
def gcd(x, y):
	while y:
		x, y = y, x % y
	return x