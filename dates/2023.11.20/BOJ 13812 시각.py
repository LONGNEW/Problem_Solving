import sys

n, k = map(int, sys.stdin.readline().split())
answer = 0

for h in range(n + 1):
    for m in range(60):
        if m == 60:
            continue
        for s in range(60):
            h, m, s = str(h), str(m), str(s)

            if len(h) == 1:
                h = "0" + h
            if len(m) == 1:
                m = "0" + m
            if len(s) == 1:
                s = "0" + s

            ret = h + m + s
            if str(k) in list(ret):
                answer += 1

print(answer)