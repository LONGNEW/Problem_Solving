# import sys
#
# n = int(sys.stdin.readline())
# data = list(map(int, sys.stdin.readline().split()))
# temp = [0]
# # 마지막에 reverse 해주기
# ans = []
#
# for i in range(n - 1, -1, -1):
#     num = data[i]
#     flag = 0
#
#     while temp:
#         compare = temp.pop()
#
#         if num < compare:
#             flag = 1
#             ans.append(compare)
#             temp.append(compare)
#             break
#
#     if not flag:
#         ans.append(-1)
#     temp.append(num)
#
# ans.reverse()
# for item in ans:
#     print(item, end=" ")

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
temp = []
ans = [-1] * n

for i in range(n):
    while temp and data[temp[-1]] < data[i]:
        ans[temp.pop()] = data[i]

    temp.append(i)

for item in ans:
    print(item, end=" ")
