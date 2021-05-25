import sys

n = int(sys.stdin.readline())
a = 1

for i in range(2, n + 1):
    a *= i

cnt = 0
while a % 10 == 0:
    cnt += 1
    a //= 10

print(cnt)