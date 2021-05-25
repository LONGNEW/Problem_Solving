import sys

m, n = map(int, sys.stdin.readline().split())
prime_num = [1] * 1000001
prime_num[1] = 0

i = 2
while i <= n:
    cnt = i + i
    while cnt <= n:
        prime_num[cnt] = 0
        cnt += i
    i += 1

for i in range(m, n + 1):
    if prime_num[i] == 1:
        print(i)
