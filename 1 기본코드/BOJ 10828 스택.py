import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    temp = sys.stdin.readline().strip()

    # push 연산.
    if " " in temp:
        temp = temp.split()
        # 숫자 문자열로 넣었음
        stack.append(temp[1])

    # pop 연산.
    if temp == 'pop':
        if len(stack) > 0:
            data = stack.pop()
            print(data)
        else:
            print(-1)

    if temp == 'size':
        print(len(stack))

    if temp == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)

    if temp == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)