import sys


def fibonachi(n):
    prev, now = 0, 1
    for i in range(n):
        prev, now = now, prev + now
    return prev

n = int(sys.stdin.readline())
print(fibonachi(n))

def fibo(x):
    if x < 2:
        return x
    return fibo(x - 1) + fibo(x - 2)
print(fibo(int(input())))