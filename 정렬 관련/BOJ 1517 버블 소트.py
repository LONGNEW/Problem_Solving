import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def merge(start, end):
    # merge
    global swap
    new_arr = []
    mid = (start + end) // 2
    l_idx, r_idx = start, mid
    cnt = 0
    while l_idx < mid and r_idx < end:
        if arr[l_idx] > arr[r_idx]:
            new_arr.append(arr[r_idx])
            r_idx += 1
            cnt += 1
        else:  # arr[idx1] < arr[idx2]
            new_arr.append(arr[l_idx])
            l_idx += 1
            swap += cnt

    while l_idx < mid:
        new_arr.append(arr[l_idx])
        l_idx += 1
        swap += cnt
    while r_idx < end:
        new_arr.append(arr[r_idx])
        r_idx += 1

    # reflect
    for t in range(len(new_arr)):
        arr[start + t] = new_arr[t]

def merge_sort(start, end):
    global swap, arr
    size = end - start
    mid = (start + end) // 2
    if size <= 1:
        return

    # divide
    merge_sort(start, mid)
    merge_sort(mid, end)
    merge(start, end)

n = int(input())
arr = list(map(int, input().split()))
swap = 0
merge_sort(0, n)
print(swap)
