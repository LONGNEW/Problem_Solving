N = int(input())
number = []
for _ in range(N):
    input_number = int(input())
    number.append(input_number)
number.sort()
for i in range(N):
    print(number[i])