import sys
from collections import deque

n = int(sys.stdin.readline())
pref_boy, pref_girl, ans_girl = dict(), dict(), dict()

boy_name = list(sys.stdin.readline().split())
girl_name = list(sys.stdin.readline().split())

for item in boy_name:
    pref_boy[item] = dict()
for item in girl_name:
    pref_girl[item] = dict()
    ans_girl[item] = 0

for _ in range(n):
    temp = list(sys.stdin.readline().split())

    for i in range(1, len(temp)):
        pref_boy[temp[0]][temp[i]] = i

for _ in range(n):
    temp = list(sys.stdin.readline().split())

    for i in range(1, len(temp)):
        pref_girl[temp[0]][temp[i]] = i

boy_name = deque(boy_name)
while boy_name:
    boy = boy_name.popleft()

    for key in pref_boy[boy].keys():
        if ans_girl[key] == 0:
            ans_girl[key] = boy
            break

        occupy = ans_girl[key]
        if pref_girl[key][occupy] > pref_girl[key][boy]:
            boy_name.append(occupy)
            ans_girl[key] = boy
            break

for item in ans_girl.keys():
    print(ans_girl[item], item)
