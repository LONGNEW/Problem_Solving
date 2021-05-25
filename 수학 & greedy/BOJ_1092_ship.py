import sys
from collections import deque

n = int(sys.stdin.readline())
crain = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))

crain.sort(key= lambda x : -x)
weight.sort(key= lambda x : -x)

if weight[0] > crain[0]:
    print(-1)
    exit(0)

cnt = 0
while len(weight) > 0:
    cnt += 1

    for item in crain:

        for i in range(len(weight)):
            if item >= weight[i]:
                del weight[i]
                break

print(cnt)