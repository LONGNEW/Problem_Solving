import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
compare_num = list(map(int, sys.stdin.readline().split()))
numbers.sort()

possible = [False] * M

for target_idx in range(len(compare_num)):
    target = compare_num[target_idx]
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            possible[target_idx] = True
            break

        if numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

for boolean in possible:
    print(1 if boolean else 0)