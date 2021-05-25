import sys

A, B = map(int, sys.stdin.readline().split())

if B > A:
    a, b = B, A
else:
    a, b = A, B

while b != 0:
    a = a % b
    a, b = b, a

print(a)
print(A * B // a)