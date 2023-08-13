class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        temp_height = [0] * length

        prev_max = 0
        for i in range(length):
            prev_max = max(prev_max, height[i])
            temp_height[i] = prev_max

        prev_max = 0
        for i in range(length - 1, -1, -1):
            if temp_height[i] == height[i]:
                break
            prev_max = max(prev_max, height[i])
            temp_height[i] = prev_max

        ret = 0
        for i in range(length):
            ret += (temp_height[i] - height[i])

        return ret

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ret = 0
#         left, right = 0, len(height) - 1
#         max_left, max_right = 0, 0
#
#         while left < right:
#             val_left, val_right = height[left], height[right]
#             if val_left > val_right:
#                 if max_right < val_right:
#                     # 새로운 가장 높은 지점을 찾은 경우
#                     # 물이 채워지지 않고 값만 업데이트
#                     max_right = val_right
#                 else:
#                     # 현재 지점은 다른 두 높은 건물에 쌓여있음
#                     # 이 떄 왼쪽은 아까 포인터가 가리킨 벽이 있고
#                     # 오른쪽은 maxRight가 있음.
#                     ret += (max_right - val_right)
#                 right -= 1
#             else:
#                 if max_left < val_left:
#                     max_left = val_left
#                 else:
#                     ret += (max_left - val_left)
#                 left += 1
#         return ret

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ret = 0
#         left, right = 0, len(height) - 1
#         max_left, max_right = 0, 0
#
#         while left < right:
#             val_left, val_right = height[left], height[right]
#             if val_left > val_right:
#                 if max_right < val_right:
#                     # 새로운 가장 높은 지점을 찾은 경우
#                     # 물이 채워지지 않고 값만 업데이트
#                     max_right = val_right
#                 else:
#                     # 현재 지점은 다른 두 높은 건물에 쌓여있음
#                     # 이 떄 왼쪽은 아까 포인터가 가리킨 벽이 있고
#                     # 오른쪽은 maxRight가 있음.
#                     ret += (min(max_right, val_left) - val_right)
#                 right -= 1
#             else:
#                 if max_left < val_left:
#                     max_left = val_left
#                 else:
#                     ret += (min(max_left, val_right) - val_left)
#                 left += 1
#         return ret