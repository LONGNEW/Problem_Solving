"""
 N(짝수)개의 학급 : M명의 학생

 홀수 - 청팀, 짝수 - 백팀
"""

import sys

n, m = map(int, sys.stdin.readline().split())
data = dict()

for i in range(1, n + 1):
    data[i] = []

while True:
    num, name = sys.stdin.readline().split()

    if num == '0' and name == '0':
        break

    num = int(num)

    if len(data[num]) == m:
        continue

    data[num].append((name, num))

odd = []
even = []

for item in data.keys():
    now = data[item]
    now.sort(key=lambda x:(len(x[0]), x[0]))

    if item % 2 == 1:
        for item in now:
            odd.append(item)
    else:
        for item in now:
            even.append(item)

for item in odd:
    print(item[1], item[0])

for item in even:
    print(item[1], item[0])
