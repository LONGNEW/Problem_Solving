import sys

n = int(sys.stdin.readline())
ans = 99999
five = n // 5

while five > 0:
    if (n - five * 5) % 3 == 0:
        ans = min(ans, five + (n - five * 5) // 3)
    five -= 1

if n % 3 == 0:
    ans = min(ans, n // 3)

print(ans if ans != 99999 else -1)