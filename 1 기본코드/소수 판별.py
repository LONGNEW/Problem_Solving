from math import sqrt

prime_number = [1] * 10001
prime_number[0] = prime_number[1] = 0

for i in range(2, int(sqrt(10001))):
#10000 까지의 소수를 구하려고 한다면 그 루트 값을 이용하는데.
#숫자가 합성수로 이뤄진다면 그 수는 두 숫자의 합이고,
# 그 중간값은 루트 값보다 크거나 작기 때문이다.
# 그래서 루트값을 포함하도록 만들어야 한다.
# https://makedotworld.tistory.com/13

    for j in range(i * i, 10001, i):

        if prime_number[j]:
            prime_number[j] = 0