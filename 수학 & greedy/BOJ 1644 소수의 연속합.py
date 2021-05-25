import sys
n = int(sys.stdin.readline())
nums = []

prime_num = [1] * (n + 1)
prime_num[0] = 0
prime_num[1] = 0

for i in range(2, n + 1):
    for j in range(i + i, n + 1, i):
        prime_num[j] = 0

for idx, item in enumerate(prime_num):
    if item:
        nums.append(idx)

start, end, ans = 0, 0, 0
if n > 1:
    temp = nums[start]

while start < len(nums):
    if temp >= n:
        if temp == n:
            ans += 1
        temp -= nums[start]
        start += 1
    else:
        if end == len(nums):
            break
        end += 1
        if end != len(nums):
            temp += nums[end]
print(ans)