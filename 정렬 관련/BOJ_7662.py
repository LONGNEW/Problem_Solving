import sys
from heapq import heappop, heappush

t = int(sys.stdin.readline())
for i in range(t):
    max_num = []
    min_num = []
    data = [0] * 1000000
    k = int(sys.stdin.readline())

    for j in range(k):
        l, n = sys.stdin.readline().split()
        n = int(n)

        if l == 'I':
            heappush(max_num, (-n, j))
            heappush(min_num, (n, j))

            data[j] = 1
        else:
            if n == -1:
                while min_num and data[min_num[0][1]] == 0:
                    heappop(min_num)

                if min_num:
                    data[min_num[0][1]] = 0
                    heappop(min_num)
            else:
                while max_num and data[max_num[0][1]] == 0:
                    heappop(max_num)

                if max_num:
                    data[max_num[0][1]] = 0
                    heappop(max_num)

    if sum(data) == 0:
        print("EMPTY")
    else:
        while max_num and data[max_num[0][1]] == 0:
            heappop(max_num)
        ans_max = -max_num[0][0]

        while min_num and data[min_num[0][1]] == 0:
            heappop(min_num)
        ans_min = min_num[0][0]

        print(f"{ans_max} {ans_min}")