
input_number = int(input())
answer = [0] * 10
while input_number >= 1:
    other = input_number % 10
    answer[other] += 1
    input_number = input_number // 10

for i in range(len(answer) - 1, -1, -1):
    for _ in range(answer[i]):
        print(i, end='')