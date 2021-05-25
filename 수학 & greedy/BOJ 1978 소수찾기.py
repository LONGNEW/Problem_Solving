import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

prime_num = [True] * 1001
prime_num[1] = False

i = 2
while i <= 1000:
    cnt = i + i
    while cnt <= 100:
        prime_num[cnt] = False
        cnt += i
    i += 1

ret = 0
for item in data:
    if prime_num[item]:
        ret += 1
print(ret)