import sys
from math import sqrt

prime_number = [1] * 300001
prime_number[0] = prime_number[1] = 0
for i in range(2, int(sqrt(300001))):
    for j in range(i * i, 300001, i):
        if prime_number[j]:
            prime_number[j] = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    ret = []
    for i in range(n + 1, 2 * n + 1):
        if prime_number[i]:
            ret.append(i)
    print(len(ret))