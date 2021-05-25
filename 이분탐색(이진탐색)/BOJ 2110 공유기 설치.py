import sys

n, c = map(int, sys.stdin.readline().split())

array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))
array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    cnt = 1
    for i in range(len(array)):
        if array[i] >= value + mid:
            value = array[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)