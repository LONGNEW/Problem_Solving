import sys

n = int(sys.stdin.readline())
ans = []
names = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]

for i in range(9):
    temp = list(map(int, sys.stdin.readline().split()))
    ans.append((max(temp), names[i]))

ans.sort()
print(ans[-1][1])