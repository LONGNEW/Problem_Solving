
while True:
    try:
        n = input()
        lower, capital, num, space = 0, 0, 0, 0
        for item in n:
            if 65 <= ord(item) <= 90:
                capital += 1
            if 97 <= ord(item) <= 122:
                lower += 1
            if item == ' ':
                space += 1
            if 48 <= ord(item) <= 57:
                num += 1
        print("{} {} {} {}".format(lower, capital, num, space))
    except EOFError:
        break