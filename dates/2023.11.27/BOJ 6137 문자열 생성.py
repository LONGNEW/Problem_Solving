import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    data.append(sys.stdin.readline().strip())

ans = []
left, right = 0, n - 1
while left <= right:
    lc, rc = data[left], data[right]

    if lc == rc:
        ll, rr = left + 1, right - 1

        while ll < rr:
            if data[ll] != data[rr]:
                break
            ll, rr = ll + 1, rr - 1

        if ll >= rr:
            ans.append(lc)
            left += 1
            continue

        if data[ll] > data[rr]:
            ans.append(rc)
            right -= 1
        else:
            ans.append(lc)
            left += 1
        continue



    if lc < rc:
        ans.append(lc)
        left += 1
    else :
        ans.append(rc)
        right -= 1

cnt = 80
for i in range(1, len(ans) + 1):
    print(ans[i - 1], end="")
    if i % cnt == 0:
        print()