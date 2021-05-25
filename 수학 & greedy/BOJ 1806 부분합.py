import sys

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
length = n + 1

front_idx = 0
back_idx = 1
temp = data[front_idx] + data[back_idx]

while front_idx < n:
    if temp >= s:
        length = min(length, back_idx - front_idx + 1)
        temp -= data[front_idx]
        front_idx += 1

    else:
        if back_idx == n and temp < s:
            break
        back_idx += 1
        if back_idx != n:
            temp += data[back_idx]

if length == n + 1:
    print(0)
else:
    print(length)