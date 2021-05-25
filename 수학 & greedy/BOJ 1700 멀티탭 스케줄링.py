import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

temp = []
ans = 0
for idx, item in enumerate(data):
    if item in temp:
        continue
    if len(temp) < n:
        temp.append(item)
        continue

    idx_list = []
    for i in range(len(temp)):
        try:
            index = data[idx:].index(temp[i])
        except:
            index = 101
        idx_list.append((index, temp[i]))

    idx_list.sort(key=lambda x:-x[0])
    index = temp.index(idx_list[0][1])
    temp.pop(index)
    temp.append(item)
    ans += 1
print(ans)
