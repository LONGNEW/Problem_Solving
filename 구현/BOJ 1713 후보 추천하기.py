import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

q, cnt, visit = [], [0] * 101, [0] * 101
for day in range(len(data)):
    person = data[day]
    length = len(q)

    if visit[person]:
        q.sort(key=lambda x:(-x[0], -x[1]))
        for i in range(length):
            if q[i][2] == person:
                break

        temp_cnt, temp_day, temp_person = q.pop(i)
        cnt[person] += 1
        q.append((cnt[person], temp_day, person))
        continue

    if length == n:
        q.sort(key=lambda x: (-x[0], -x[1]))
        temp_cnt, temp_day, temp_person = q.pop()
        visit[temp_person] = 0
        cnt[temp_person] = 0

    cnt[person] += 1
    visit[person] = 1
    q.append((cnt[person], day, person))

ans = []
for a, b, c in q:
    ans.append(c)

ans.sort()
print(*ans)