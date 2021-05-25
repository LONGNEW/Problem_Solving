def gcd(n, m):
	if n < m:
		n, m = m, n
	while m != 0:
		n, m = m, n % m
	return n
--------------------------------------------------------------
import sys
from math import gcd

n, m = map(int, sys.stdin.readline().split())
cnt = gcd(n, m)
for i in range(cnt):
    print(1, end="")