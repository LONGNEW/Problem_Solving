import sys
from math import sqrt

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


r, g = map(int, sys.stdin.readline().split())
factor = gcd(r, g)
factor_list = set()

for i in range(1, int(sqrt(factor) + 1)):
    if factor % i == 0:
        factor_list.add(i)
        factor_list.add(factor // i)

for item in factor_list:
    print(item, r // item, g // item)