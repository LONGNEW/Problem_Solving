"""
    N개의 숫자 -> 다양한 수
    수의 합으로 만들 수 없는 수의 개수.
"""

import sys
from itertools import combinations

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
limit = sum(data)
temp = dict()

for pick in range(1, n + 1):
    for count in combinations(data, pick):
        now = sum(count)

        if now not in temp:
            temp[now] = 1
            limit -= 1

print(limit)