import sys

n = int(sys.stdin.readline())
man = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    man.append((int(age), name))

man = sorted(man, key=lambda x : x[0])

for item in man:
    print(*item)