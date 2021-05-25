import sys

data = list(map(int, sys.stdin.readline().split()))
cal = [1, 1, 1]
cnt = 1
while data != cal:
    for i in range(len(cal)):
        cal[i] += 1

    if cal[0] == 16:
        cal[0] = 1
    if cal[1] == 29:
        cal[1] = 1
    if cal[2] == 20:
        cal[2] = 1
    cnt += 1
print(cnt)