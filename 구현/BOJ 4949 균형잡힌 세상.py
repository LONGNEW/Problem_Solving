import sys

while True:
    data = sys.stdin.readline().rstrip()
    if data == ".":
        break

    ans = []
    for item in data:
        if item == "(" or item == "[":
            ans.append(item)

        elif item == ")":
            if len(ans) == 0:
                print("no")
                break

            if ans[-1] != "(":
                print("no")
                break
            else:
                ans.pop()

        elif item == "]":
            if len(ans) == 0:
                print("no")
                break
            if ans[-1] != "[":
                print("no")
                break
            else:
                ans.pop()
    else:
        print("yes" if len(ans) == 0 else "no")
