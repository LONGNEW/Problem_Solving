import sys

n = sys.stdin.readline().strip()
alphabet = [-1] * 26

for idx, item in enumerate(n):
    if alphabet[ord(item) - 97] == -1:
        alphabet[ord(item) - 97] = idx

for item in alphabet:
    print(item, end=" ")