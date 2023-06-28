import sys

route =((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))
c = []
start = input()
c.append(start)

for i in range(35):
    a = input()
    if a in c:
        print("Invalid")
        sys.exit(0)
    c.append(a)

    now, prev = c[i], c[i + 1]
    move = (ord(now[0]) - ord(prev[0]), int(now[1]) - int(prev[1]))
    if move not in route:
        print("Invalid")
        sys.exit(0)

start, end = c[0], c[-1]
move = (ord(end[0]) - ord(start[0]), int(end[1]) - int(start[1]))

if move not in route:
    print("Invalid")
    sys.exit(0)

print("Valid")