N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_idx = 0
B_idx = 0
answer = []
while A_idx < len(A) and B_idx < len(B):
    if A[A_idx] < B[B_idx]:
        answer.append(A[A_idx])
        A_idx += 1
    elif A[A_idx] > B[B_idx]:
        answer.append(B[B_idx])
        B_idx += 1
    else:
        answer.append(A[A_idx])
        answer.append(A[A_idx])
        A_idx += 1
        B_idx += 1

if A_idx == len(A):
    answer = answer + B[B_idx:]
else:
    answer += A[A_idx:]

for number in answer:
    print(number, end=" ")