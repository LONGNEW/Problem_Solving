import sys
from math import sqrt

prime_number = [1] * 10001
prime_number[0] = prime_number[1] = 0
for i in range(2, int(sqrt(10001))):
    for j in range(i * i, 10001, i):
        if prime_number[j]:
            prime_number[j] = 0

ret = []
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

for i in range(m, n + 1):
    if prime_number[i]:
        ret.append(i)

if len(ret) <= 0:
    print(-1)
else:
    print(sum(ret))
    print(ret[0])