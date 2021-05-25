import sys

data = list(sys.stdin.readline().strip())
temp = []

for i in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().strip()

    if cmd[0] == 'P':
        cmd = cmd.split()
        data.append(cmd[1])

    elif cmd == 'L':
        if len(data) > 0:
            temp.append(data.pop())
            
    elif cmd == 'D':
        if len(temp) > 0:
            data.append(temp.pop())
            
    else:
        if len(data) > 0:
            data.pop()

temp.reverse()
data += temp
print("".join(data))