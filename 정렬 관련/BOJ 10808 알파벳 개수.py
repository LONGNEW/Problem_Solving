import sys

n = sys.stdin.readline().strip()
alphabet = [0] * 26

for item in n:
    alphabet[ord(item) - 97] += 1

for item in alphabet:
    print(item, end=" ")