import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
button = list(sys.stdin.readline().strip())


def check(num):
    for item in num:
        if item in button:
            return False
    return True


cnt = abs(n - 100)
for i in range(1000001):
    str_num = str(i)
    if check(str_num):
        cnt = min(cnt, len(str_num) + abs(i - n))
print(cnt)