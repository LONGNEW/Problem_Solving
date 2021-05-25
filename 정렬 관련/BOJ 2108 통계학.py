import sys
from collections import Counter

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))

if sum(data) / n  - sum(data) // n >= 0.5:
    print((sum(data) // n) + 1)
else:
    print(sum(data) // n)

sort_data = sorted(data)
idx = n // 2
print(sort_data[idx])

count = Counter(data)
temp = count.most_common()
temp.sort(key=lambda x:(-x[1], x[0]))
if n >= 2:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])

print(max(data) - min(data))