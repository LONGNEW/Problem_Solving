import sys
from math import sqrt

prime_number = [1] * 1004000
prime_number[0] = prime_number[1] = 0
for i in range(2, int(sqrt(1004000))):
    for j in range(i * i, 1004000, i):
        if prime_number[j]:
            prime_number[j] = 0


def palindrome(n):
    n = str(n)
    start = 0
    end = len(n) - 1
    while start < end:
        if n[start] != n[end]:
            return 0
        start += 1
        end -= 1
    return 1

n = int(sys.stdin.readline())
for i in range(n, 1004000):
    if palindrome(i) and prime_number[i]:
        print(i)
        break