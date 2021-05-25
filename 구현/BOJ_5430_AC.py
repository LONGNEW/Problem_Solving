import sys

t = int(sys.stdin.readline())
for i in range(t):
    command = sys.stdin.readline().strip().replace('RR', '')
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().strip()[1:-1].split(",")
    r, f, b = 0, 0, 0

    for item in command:
        if item == 'R':
            r += 1
        else:
            if r % 2 == 0:
                f += 1
            else:
                b += 1

    if f + b <= n:
        data = data[f: n - b]

        if r % 2 == 1:
            print('[' + ','.join(data[::-1]) + ']')
        else:
            print('[' + ','.join(data) + ']')
    else:
        print('error')