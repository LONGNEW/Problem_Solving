import sys

def minFactor(a, b):
    num = 2
    ret = 1
    while a >= num and b >= num:
        if a % num == 0 and b % num == 0:
            a //= num
            b //= num
            ret *= num
        else:
            num += 1
    return ret

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(data)):
    item = data[i]
    temp_num = data[0]
    divisior = minFactor(temp_num, item)
    string = str(temp_num // divisior) + '/' + str(item // divisior)
    print(string)


