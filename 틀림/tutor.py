import math


def solution(n, k):
    num = ""
    while n > 0:
        num += str(n % k)
        n //= k
    num = num[::-1]

    temp = list(num.split('0'))
    answer = 0

    for item in temp:
        if item == "" or item == "1":
            continue

        item = int(item)
        prime = True

        for i in range(2, int(math.sqrt(item)) + 1):
            if item % i == 0:
                prime = False
                break

        if prime:
            answer += 1

    return answer

print(solution(1000000, 10))