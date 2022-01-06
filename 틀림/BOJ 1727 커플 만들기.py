import sys

n, m = map(int, sys.stdin.readline().split())
man = list(map(int, sys.stdin.readline().split()))
woman = list(map(int, sys.stdin.readline().split()))

if n > m:
    n, m = m, n
    man, woman = woman, man
man.sort()
woman.sort()
ans = [float('inf')] * n

for i in range(m - n + 1):
    temp, change = [], 1

    for j in range(n):
        ret = abs(man[j] - woman[i + j])
        if ans[j] < ret:
            change = 0
            break
        temp.append(ret)

    if change:
        ans = []
        for item in temp:
            ans.append(item)
print(sum(ans))