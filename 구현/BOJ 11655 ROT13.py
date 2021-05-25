import sys

sentence = sys.stdin.readline().rstrip()
new = []

for item in sentence:
    alphabet = ord(item)

    if 65 <= alphabet <= 90:
        alphabet += 13

        if alphabet > 90:
            temp = alphabet - 90
            alphabet = 64 + temp
        new.append(chr(alphabet))

    elif 97 <= alphabet <= 122:
        alphabet += 13
        if alphabet > 122:
            temp = alphabet - 122
            alphabet = 96 + temp
        new.append(chr(alphabet))

    else:
        new.append(item)
print("".join(new))