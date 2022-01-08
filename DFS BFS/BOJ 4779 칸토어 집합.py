import sys
sys.setrecursionlimit(100000)

def Cantor(three_list):
    if len(three_list) <= 1:
        return three_list

    branch = len(three_list) // 3
    fir_section = Cantor(three_list[:branch])
    sec_section = ' ' * branch
    thr_section = Cantor(three_list[branch * 2:])

    return fir_section + sec_section + thr_section

while True:
    try:
        N = 3 ** int(input())
        threes = '-' * N

        hypen = Cantor(threes)
        print("".join(hypen))

    except EOFError:
        break
