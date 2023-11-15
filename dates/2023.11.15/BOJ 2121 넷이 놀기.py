import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
data = dict()

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data[(x, y)] = i

answer = dict()
dx = [
    [-a, -a, 0],
    [a, a, 0]
]
dy = [
    [0, b, b],
    [0, -b, -b]
]

for key in data.keys():
    x, y = key
    use_dx, use_dy = None, None

    for i in range(2):
        use_dx = dx[i]
        for j in range(2):
            use_dy = dy[i]

            dots = [data[key]]
            for idx in range(3):
                nx, ny = x + use_dx[idx], y + use_dy[idx]
                if (nx, ny) not in data:
                    break
                dots.append(data[(nx, ny)])

            dots.sort()
            if len(dots) == 4:
                answer[tuple(dots)] = 1

print(len(answer))