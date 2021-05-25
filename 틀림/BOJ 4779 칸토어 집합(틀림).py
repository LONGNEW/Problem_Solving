def Cantor(three_list):

    if len(three_list) <= 1:
        return three_list

    branch = len(three_list) // 3
    fir_section = Cantor(three_list[:branch])
    thr_section = Cantor(three_list[branch * 2:])

    sec_section = ''
    for i in range(branch):
        sec_section += ' '

    return fir_section + sec_section + thr_section

while True:
    try:
        N = int(input())
    except EOFError:
        break
    # 0일 경우.
    # len_of_three
    len_of_three = 1
    for i in range(N):
        len_of_three *= 3
    threes = ''
    for _ in range(len_of_three):
        threes += '-'
    hypen = Cantor(threes)
    for i in range(len(hypen)):
         print(hypen[i], end= "")