import sys

n = int(sys.stdin.readline())
ans = 0

for i in range(n):
    idx = [0] * 26
    data = sys.stdin.readline().strip()
    now = data[0]
    flag = 0

    for item in data:
        if now != item and idx[ord(item) - ord('a')] > 0:
            flag = 1
            break

        if now != item:
            now = item

        idx[ord(item) - ord('a')] += 1

    if flag == 0:
        ans += 1
print(ans)