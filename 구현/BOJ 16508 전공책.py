import sys
from itertools import combinations

def make():
    global ans
    for i in range(26):
        if check[i] > temp[i]:
            return

    ans = min(ans, total)

target = sys.stdin.readline().rstrip().upper()
check = [0] * 26
for item in target:
    check[ord(item) - 65] += 1

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    value, word = sys.stdin.readline().split()
    value = int(value)
    word = word.upper()
    data.append((value, word))

ans = float("inf")
for i in range(1, n + 1):

    for idxs in list(combinations(range(n), i)):
        temp = [0] * 26
        total = 0
        for j in idxs:
            value, word = data[j]
            total += value

            for item in word:
                temp[ord(item) - 65] += 1
        make()

if ans == float("inf"):
    print(-1)
    exit(0)
    
print(ans)