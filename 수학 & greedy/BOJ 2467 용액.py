import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(data) - 1

ret = [0, 0]
val, flag = 9999999999999, 1

while start < end:
    mix = data[start] + data[end]
    if abs(mix) < val:
        ret = [data[start], data[end]]
        val = abs(mix)
    if mix > 0:
        end -= 1
    elif mix < 0:
        start += 1
    else:
        print(data[start], data[end])
        flag = 0
        break
if flag:
    print(ret[0], ret[1])