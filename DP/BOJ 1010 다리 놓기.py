import sys
from math import factorial

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    ans = factorial(m) // (factorial(m - n) * factorial(n))
    print(ans)