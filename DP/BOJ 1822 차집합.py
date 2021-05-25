import sys

a, b = map(int, sys.stdin.readline().split())
set_a = set(map(int, sys.stdin.readline().split()))
set_b = set(map(int, sys.stdin.readline().split()))

ans = list(set_a - set_b)
ans.sort()
print(len(ans))
for item in ans:
    print(item, end=" ")