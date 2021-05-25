import sys

n = int(sys.stdin.readline())

for i in range(n):
    string = sys.stdin.readline().strip()
    left = 0
    right = 0
    flag = 1
    for item in string:
        if item == '(':
            left += 1
        else:
            left -= 1
            if left < 0:
                flag = 0
                break

    if flag:
        if left != 0:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
