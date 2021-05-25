import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, sys.stdin.readline().split())
gcd = gcd(a, b)
print(gcd * int(a / gcd) * int(b / gcd))
