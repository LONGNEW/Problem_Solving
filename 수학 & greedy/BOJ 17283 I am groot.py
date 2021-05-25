import math
L = int(input())
R = int(input())
total = 0
cnt = 2
while 1:
    L = int(L * (R / 100))
    if L <= 5:
        break
    total += (cnt * L)
    cnt *= 2
print(total)
