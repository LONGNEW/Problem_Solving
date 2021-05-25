import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

ans = a * b * c
data = [0] * 10

while ans > 0:
    idx = ans % 10
    data[idx] += 1
    ans //= 10

for item in data:
    print(item)