N = int(input())
number = {}
for i in range(N):
    data = int(input())
    if data in number:
        number[data] += 1
    else:
        number[data] = 1
answer = sorted(number.items(), key = lambda x : (-x[1], x[0]))
print(answer[0][0])

import sys
from collections import Counter

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))

cnt = Counter(sorted(data)).most_common(1)
print(cnt[0][0])