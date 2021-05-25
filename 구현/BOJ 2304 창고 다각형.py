import sys

N = int(sys.stdin.readline())
buliding = [0] * 1001
data_list = []
for i in range(N):
    L, H = map(int, sys.stdin.readline().split())
    buliding[L] = H
    data_list.append((L, H))

data_list.sort(key= lambda x:-(x[0]))
last_idx = data_list[0][0]
data_list.sort(key= lambda x:x[0])
start_idx = data_list[0][0]
data_list.sort(key= lambda x:-(x[1]))
biggest_idx = data_list[0][0]

total = 0

idx = start_idx
height = 0
while idx < biggest_idx:
    height = max(buliding[idx], height)
    total += height
    idx += 1

idx = last_idx
height = 0
while idx > biggest_idx:
    height = max(buliding[idx], height)
    total += height
    idx -= 1

print(total + buliding[biggest_idx])