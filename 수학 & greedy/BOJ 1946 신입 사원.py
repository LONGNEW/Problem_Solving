import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = [0] * (n + 1)
    for j in range(n):
        bio, interview = map(int, sys.stdin.readline().split())
        data[bio] = interview

    max_interview_rank = data[1]
    cnt = 1

    for j in range(1, n + 1):
        if data[j] < max_interview_rank:
            cnt += 1
            max_interview_rank = data[j]
    print(cnt)
