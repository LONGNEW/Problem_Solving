import sys

data = list(sys.stdin.readline().strip())
target = list(sys.stdin.readline().strip())

ans = []

for item in data:
    ans.append(item)

    if len(ans) >= len(target):
        start = len(ans) - 1
        for i in range(len(target) - 1, -1, -1):
            if ans[start] != target[i]:
                break
            start -= 1
        else:
            for i in range(len(target)):
                ans.pop(-1)

ans = "".join(ans)
print(ans if len(ans) > 0 else "FRULA")