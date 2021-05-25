import sys
sys.setrecursionlimit(100000)

def dfs(num, count):
    global cnt, flag
    if num == b:
        flag = 1
        cnt = min(cnt, count)
        return

    word = str(num) + '1'
    if int(word) <= b:
        dfs(int(word), count + 1)
    if num * 2 <= b:
        dfs(num * 2, count + 1)


a, b = map(int, sys.stdin.readline().split())
flag = 0
cnt = float('inf')
dfs(a, 0)

print(cnt + 1 if flag else -1)