import sys

n = int(sys.stdin.readline())
# data = [[] for i in range(n)]
# for i in range(n):
#     temp = sys.stdin.readline().split()
#     data[i].append(temp[0])
#     for j in range(1, len(temp)):
#         data[i].append(int(temp[j]))
# data.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
# for item in data:
#     print(item[0])
data = []
for i in range(n):
    name, korean, eng, math = sys.stdin.readline().split()
    data.append((name, int(korean), int(eng), int(math)))
data.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for item in data:
    print(item[0])