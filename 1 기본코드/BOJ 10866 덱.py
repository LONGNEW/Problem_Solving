import sys

n = int(sys.stdin.readline())
deck = []

for i in range(n):
    temp = sys.stdin.readline().strip()

    # push 연산.
    if " " in temp:
        temp = temp.split()
        # 숫자 문자열로 넣었음
        if temp[0] == 'push_front':
            deck = [temp[1]] + deck
        else:
            deck.append(temp[1])

    # pop 연산.
    if temp == 'pop_front':
        if len(deck) > 0:
            print(deck[0])
            del deck[0]
        else:
            print(-1)

    if temp == 'pop_back':
        if len(deck) > 0:
            print(deck[-1])
            del deck[-1]
        else:
            print(-1)

    if temp == 'size':
        print(len(deck))

    if temp == 'empty':
        if len(deck) > 0:
            print(0)
        else:
            print(1)

    if temp == 'front':
        if len(deck) > 0:
            print(deck[0])
        else:
            print(-1)

    if temp == 'back':
        if len(deck) > 0:
            print(deck[-1])
        else:
            print(-1)