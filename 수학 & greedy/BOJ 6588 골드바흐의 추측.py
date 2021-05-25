import sys

num = [1] * 1000001
num[1] = 0
num[0] = 0
for i in range(2, 1000001):
    for j in range(i + i, 1000001, i):
        num[j] = 0

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break

    res = []
    for i in range(3, n, 2):
        if num[i] == 1:
            if num[n - i] == 1:
                res.append((i, n - i, n - i - i))
                break

    if len(res) == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print("{} = {} + {}".format(n, res[0][0], res[0][1]))