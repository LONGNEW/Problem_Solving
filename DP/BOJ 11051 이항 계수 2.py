# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# up, down_1, down_2 = 1, 1, 1
#
# for i in range(2, n + 1):
#     up *= i
#
# for i in range(2, k + 1):
#     down_1 *= i
#
# for i in range(2, n - k + 1):
#     down_2 *= i
#
# ans = up // (down_1 * down_2)
# print(ans % 10007)

import sys
from math import factorial

n, k = map(int, sys.stdin.readline().split())
ans = factorial(n) // (factorial(n - k) * factorial(k))
print(ans % 10007)