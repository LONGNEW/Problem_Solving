# import sys
#
# n = int(sys.stdin.readline())
# heights = list(map(int, sys.stdin.readline().split()))
# temp = []
# ans = []
#
# for idx, item in enumerate(heights):
#     flag = 0
#
# 	# 모든 temp에 들어있는 건물들을 비교하다가.
#     while temp:
#         compare_idx, compare_height = temp.pop()
#         # 크거나 같은 것을 찾은 경우에 break로 빠져나감.
#         if compare_height >= item:
#             flag = 1
#             break
#
#     if flag:
#     # compare 변수에 이 값들이 남아 있으니까 다시 temp 변수에 넣어주고,
#     # 답을 업데이트 해준다.
#         temp.append((compare_idx, compare_height))
#         ans.append(compare_idx + 1)
#     else:
#         ans.append(0)
#
#     # 현재까지의 값도 temp에 넣어주어서 비교대상이 되도록 한다.
#     temp.append((idx, item))
#
# for item in ans:
#     print(item, end=" ")

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
temp = []
ans = [0] * n

for i in range(n):
    while temp and data[temp[-1]] < data[i]:
        temp.pop()

    if temp:
        ans[i] = temp[-1] + 1
    else:
        ans[i] = 0

    temp.append(i)

for item in ans:
    print(item, end=" ")