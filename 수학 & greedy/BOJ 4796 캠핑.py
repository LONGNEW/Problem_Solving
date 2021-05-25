import sys

idx = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and P == 0:
        break

    ans = (V // P) * L
    if V % P >= L:
        ans += L
    else:
        ans += (V % P) % L
    print("Case " + str(idx) + ":", ans)
    idx += 1