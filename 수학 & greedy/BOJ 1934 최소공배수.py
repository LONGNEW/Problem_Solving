import sys
from math import gcd

t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    data = gcd(a, b)
    print(data * (a // data) * (b // data))