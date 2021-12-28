import sys, re

temp = list(sys.stdin.readline().split())
p = re.compile("[.-]")

for item in temp:
    data = p.split(item)
    print(data)