import sys
from collections import deque

cnts = dict()
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = "32123333113133122212112221"

for i in range(len(alpha)):
    cnts[alpha[i]] = cnt[i]

data = list(sys.stdin.readline().rstrip())
for i in range(len(data)):
    data[i] = int(cnts[data[i]])

data = deque(data)
temp = []

while len(data) > 1:
    length = len(data)

    while length > 1:
        word_1 = data.popleft()
        word_2 = data.popleft()

        temp.append(word_1 + word_2)
        length -= 2

    if length:
        word = data.popleft()
        temp.append(word)

    data = deque(temp)
    temp = []

if data[0] % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")