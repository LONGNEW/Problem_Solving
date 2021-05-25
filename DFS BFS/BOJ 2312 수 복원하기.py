import sys
from math import sqrt
from collections import Counter

minFactor = [i for i in range(100001)]
for i in range(2, int(sqrt(100001))):
    for j in range(i * i, 100001, i):
        if minFactor[j] == j:
            minFactor[j] = i

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    ret = []
    while n > 1:
        ret.append(minFactor[n])
        n //= minFactor[n]
        
    prime_numbers = Counter(ret)
    temp = prime_numbers.most_common()
    temp.sort()
    
    for key, value in temp:
        print(key, value)