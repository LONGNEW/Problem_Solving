import sys

n = int(sys.stdin.readline())


def solve(n):
    if n == 0:
        return '0'
    else:
        if n % 2 == 0:
            return solve(n // -2) + '0'
        else:
            return solve(n // (-2) + 1) + '1'


ans = solve(n)
if ans == '0':
    print(ans)
else:
    print(ans[1:])