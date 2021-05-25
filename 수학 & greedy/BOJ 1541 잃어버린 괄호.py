import sys

data = list(sys.stdin.readline().rstrip().split("-"))
temp = []

while data:
    now = data.pop(0)

    if '+' in now:
        in_temp = list(map(int, now.split("+")))
        ret = in_temp.pop(0)

        while in_temp:
            a = in_temp.pop(0)
            ret += a

        temp.append(ret)
    else:
        temp.append(int(now))

ans = temp.pop(0)

while temp:
    now = temp.pop(0)
    ans -= now

print(ans)