import sys

while True:
    try:
        l, a = map(int, input().split())
        ids, left, right = [], [], []

        for _ in range(a):
            x, tow = sys.stdin.readline().split()
            x = int(x)
            ids.append(x)

            if tow == "L":
                left.append(x)
            else:
                right.append(l - x)

        ids.sort()
        left.sort()
        right.sort(reverse=True)

        move = left + right
        ans = [(move[i], ids[i]) for i in range(a)]

        ans.sort()
        if len(ans) >= 2 and ans[-1][0] == ans[-2][0]:
            p = min(ans[-1][1], ans[-2][1])
            q = max(ans[-1][1], ans[-2][1])
            print(f"The last ant will fall down in {ans[-1][0]} seconds - started at {p} and {q}.")
        else:
            print(f"The last ant will fall down in {ans[-1][0]} seconds - started at {ans[-1][1]}.")
    except EOFError:
        break