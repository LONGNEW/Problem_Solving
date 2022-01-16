import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    book, data = [0] * (n + 1), []

    for i in range(1, m + 1):
        a, b = map(int, sys.stdin.readline().split())
        data.append((a, b))

    data.sort(key=lambda x:x[1])
    for a, b in data:

        for i in range(a, b + 1):
            if book[i] == 0:
                book[i] = 1
                break

    print(sum(book))