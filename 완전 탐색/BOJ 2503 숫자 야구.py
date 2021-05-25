import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    a, b, c = sys.stdin.readline().split()
    data.append((a, b, c))

ans = 0
for i in range(123, 988):
    temp = str(i)
    flag = 1

    if temp[0] == temp[1] or temp[0] == temp[2] or temp[2] == temp[1] or temp[1] == "0" or temp[2] == "0":
        continue

    for word, word_s, word_b in data:
        strike, ball = 0, 0
        for idx, item in enumerate(temp):

            if temp[idx] == word[idx]:
                strike += 1
                continue

            if item in word:
                ball += 1

        if strike != int(word_s) or ball != int(word_b):
            flag = 0

    if flag == 1:
        ans += 1
print(ans)
