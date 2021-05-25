import sys

stick = sys.stdin.readline().strip()
cnt = 0
total = 0
for idx, item in enumerate(stick):
    if item == '(':
        cnt += 1
    else:
        if stick[idx - 1] == '(':
            cnt -= 1
            total += cnt
        else:
            cnt -= 1
            total += 1
print(total)

