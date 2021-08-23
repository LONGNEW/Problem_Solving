import sys
sys.setrecursionlimit(100000)

def make(val, idx):
    global max_val, min_val
    if idx == n:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return

    if oper[0] != 0:
        oper[0] -= 1
        make(val + data[idx], idx + 1)
        oper[0] += 1

    if oper[1] != 0:
        oper[1] -= 1
        make(val - data[idx], idx + 1)
        oper[1] += 1

    if oper[2] != 0:
        oper[2] -= 1
        make(val * data[idx], idx + 1)
        oper[2] += 1

    if oper[3] != 0:
        oper[3] -= 1

        if val < 0:
            val = -val
            make(-(val // data[idx]), idx + 1)
        else:
            make(val // data[idx], idx + 1)

        oper[3] += 1


n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
max_val, min_val = -float('inf'), float('inf')

make(data[0], 1)
print(max_val)
print(min_val)