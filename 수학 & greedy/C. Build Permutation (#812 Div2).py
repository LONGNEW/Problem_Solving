import sys
import math

def check_valid(target):
    while (target ** 2) - i >= n or numbers[(target ** 2) - i] == 0:
        target -= 1

    return target ** 2

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    numbers, ans = [1] * n, [0] * n

    target = round(math.sqrt(n))
    for i in range(n - 1, -1, -1):
        square = check_valid(target)
        ans[i] = square - i
        numbers[square - i] -= 1

    if min(ans) != 0:
        print(-1)
    else:
        print(*ans)