import sys

n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    data = sys.stdin.readline().strip()
    check = dict()

    flag = 1
    for i in range(len(data)):
        alpha = data[i]
        if alpha not in check:
            check[alpha] = i
            continue

        if check[alpha] != i - 1:
            flag = 0
            break
        check[alpha] = i

    if flag:
        cnt += 1
print(cnt)