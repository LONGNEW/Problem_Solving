import sys
from math import sqrt

prime_number = [1] * 10001
prime_number[0] = prime_number[1] = 0
for i in range(2, int(sqrt(10001))):
    for j in range(i * i, 10001, i):
        if prime_number[j]:
            prime_number[j] = 0


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    ret = []

    for j in range(2, n // 2 + 1):
        temp = n - j
        if prime_number[j] and prime_number[temp]:
            ret.append((j, n - j))
    print(ret[-1][0], ret[-1][1])