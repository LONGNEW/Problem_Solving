import sys

n, k = map(int, sys.stdin.readline().split())
data = []
xs = []
ys = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    data.append(temp)

for i in range(n):
    xs.append(data[i][0])
    ys.append(data[i][1])

data.sort(key=lambda x:x[2])

ans = 9999999999
for x in xs:
    for y in ys:
        z = 0
        cnt = 0
        for i in range(n):
            if data[i][0] <= x and data[i][1] <= y:
                cnt += 1
                z = data[i][2]
                if cnt == k:
                    break
        if cnt == k:
            ans = min(ans, x + y + z)
print(ans)