import sys

length = int(sys.stdin.readline())
node = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    node.append((min(x, y), max(x, y)))

for i in range(3):
    x, y = node[i]
    if x == y:
        continue

    mid = (x + y) / 2
    if length - mid <= mid:
        length = mid
        for j in range(i, 3):
            left, right = node[j]

            if mid < left:
                left = mid - (left - mid)
            if mid < right:
                right = mid - (right - mid)

            node[j] = (min(left, right), max(left, right))
    else:
        length -= mid
        for j in range(i + 1, 3):
            left, right = node[j]

            # 시작점(mid)을 0으로 두기 위해 좌표들을 이동시킴.
            left = mid - left if left < mid else left - mid
            right = mid - right if right < mid else right - mid

            node[j] = (min(left, right), max(left, right))
print(length)