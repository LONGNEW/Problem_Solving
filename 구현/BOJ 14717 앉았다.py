import sys

a, b = map(int, sys.stdin.readline().split())

data = [2] * 11
data[0] = 0

data[a] -= 1
data[b] -= 1

temp = []
for idx, item in enumerate(data):
    for i in range(item):
        temp.append(idx)

ans = 0
all = 0
for i in range(len(temp)):
    for j in range(i + 1, len(temp)):
        all += 1
        opposite_1, opposite_2 = temp[i], temp[j]

        if a == b:
            if opposite_1 != opposite_2:
                ans += 1
            else:
                if a > opposite_2:
                    ans += 1

        else:
            if opposite_1 == opposite_2:
                continue
            my_num = a + b % 10
            opposite = opposite_1 + opposite_2 % 10
            if my_num > opposite:
                ans += 1

print("{:.3f}".format(ans / all))
