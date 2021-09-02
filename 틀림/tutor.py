data = ["A", "E", "I", "O", "U"]
word = []

def make_word(now):
    if len(now) == 6:
        return

    if len(now) > 0:
        word.append(now)

    for i in range(5):
        make_word(now + data[i])


make_word("")
word.sort()

print(len(word))