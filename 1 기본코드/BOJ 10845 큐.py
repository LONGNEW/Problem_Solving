import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    temp = sys.stdin.readline().strip()

    # push 연산.
    if " " in temp:
        temp = temp.split()
        # 숫자 문자열로 넣었음
        queue.append(temp[1])

    # pop 연산.
    if temp == 'pop':
        if len(queue) > 0:
            print(queue[0])
            del queue[0]

        else:
            print(-1)

    if temp == 'size':
        print(len(queue))

    if temp == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)

    if temp == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)

    if temp == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)