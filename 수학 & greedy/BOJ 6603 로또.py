import sys
from itertools import combinations

data = list(map(int, sys.stdin.readline().split()))
while data[0] != 0:
    num = data[1:]
    for item in combinations(num, 6):
        print(*item)
    print()
    data = list(map(int, sys.stdin.readline().split()))