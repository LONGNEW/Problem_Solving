import sys

def check():
    for fir in range(len(vacant) - 2):
        for sec in range(fir + 1, len(vacant) - 1):
            for thi in range(sec + 1, len(vacant)):
                data[vacant[fir][0]][vacant[fir][1]] = 'O'
                data[vacant[sec][0]][vacant[sec][1]] = 'O'
                data[vacant[thi][0]][vacant[thi][1]] = 'O'

                if search():
                    return True

                data[vacant[fir][0]][vacant[fir][1]] = 'X'
                data[vacant[sec][0]][vacant[sec][1]] = 'X'
                data[vacant[thi][0]][vacant[thi][1]] = 'X'
    return False

def search():
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    for idx in range(len(teacher)):

        for i in range(4):
            nx, ny = teacher[idx][0], teacher[idx][1]

            while nx >= 0 and nx < n and ny >= 0 and ny < n:
                if data[nx][ny] == 'S':
                    return False

                if data[nx][ny] == 'O':
                    break

                nx += dx[i]
                ny += dy[i]
    return True


n = int(sys.stdin.readline())
data, vacant, teacher = [], [], []

for i in range(n):
    temp = list(sys.stdin.readline().split())
    data.append(temp)

    for j in range(n):
        if temp[j] == 'T':
            teacher.append((i, j))
        elif temp[j] == 'X':
            vacant.append((i, j))

print("YES" if check() else "NO")