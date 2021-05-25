import sys

num = sys.stdin.readline().strip()
res = []
for temp in num:
    data = int(temp)
    for i in range(2, -1, -1):
        res.append(data // (2 ** i))
        data %= (2 ** i)
if int(num) == 0:
    print(0)
else:
    if res[0] == 0 and res[1] == 0:
        for i in range(2, len(res)):
            print(res[i], end="")
    elif res[0] == 0:
        for i in range(1, len(res)):
            print(res[i], end="")
    else:
        for i in range(0, len(res)):
            print(res[i], end="")

--------------------------------------------------------------
import sys
num = int(sys.stdin.readline().strip(), 8)
print("{:b}".format(num))