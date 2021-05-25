import sys

data = sys.stdin.readline().strip()
num = []
for i in range(len(data) - 1, -1, -1):
    num.append(int(data[i]))
res = []

while len(num) % 3 != 0:
    num.append(0)

num.reverse()
for i in range(0, len(num), 3):
    temp = num[i] * 4 + num[i + 1] * 2 + num[i + 2]
    res.append(temp)
for i in res:
    print(i, end="")
#
# --------------------------------------------------------------
# import sys
#
# data = int(sys.stdin.readline().strip(), 2)
# print('{:o}'.format(data))
