import sys

alpha = [0] * 26
n = int(sys.stdin.readline())
for i in range(n):
    string = sys.stdin.readline().strip()

    for j in range(len(string)):
        pos = len(string) - j - 1
        word = ord(string[j]) - ord('A')
        alpha[word] += 10 ** pos

alpha.sort(key=lambda x:-x)
ans = 0
for i in range(9, -1, -1):
    ans += alpha[9 - i] * i
print(ans)
