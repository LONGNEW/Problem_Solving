import sys
sys.setrecursionlimit(100000)

def dfs(array):
    if len(array) == 1:
        print(array[0])
        return

    if len(array) < 1:
        return

    root = array[0]
    mid = len(array)
    for i in range(1, len(array)):
        if array[i] > root:
            mid = i
            break
    dfs(array[1:mid])
    dfs(array[mid:])
    print(root)


data = []
while True:
    try:
        temp = int(input())
        data.append(temp)
    except EOFError:
        break
dfs(data)