import sys

n = sys.stdin.readline().rstrip()
middle = len(n) // 2
left, right = map(int, n[:middle]), map(int, n[middle:])

print("LUCKY" if sum(left) == sum(right) else "READY")