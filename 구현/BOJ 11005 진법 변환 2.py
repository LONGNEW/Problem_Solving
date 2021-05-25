import sys

n, b = map(int, sys.stdin.readline().split())
res = []
if n == 0:
    res.append(0)

while n != 0:
    temp = n % b
    if temp < 10:
        res.append(temp)
    else:
        temp += 55
        res.append(chr(temp))
    n //= b

res.reverse()
for item in res:
    print(item, end="")