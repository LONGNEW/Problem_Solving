import sys

n, k = map(int, sys.stdin.readline().split())
data = list(sys.stdin.readline().strip())

temp, cnt = [], k

for i in range(n):
    # 문자열에서 삭제할 것은 k번이니까 그만큼 while문에 걸리게 됨.
    # 답으로 가지고 가는 배열이 temp니까 temp가 존재하고,
    # 새로 들어올 문자가 이전에 존재하던거 보다 클 때, 답이 된다.
    while cnt > 0 and len(temp) > 0 and temp[-1] < data[i]:
        temp.pop()
        cnt -= 1

    # 그리고 삭제할 것들을 다 지우면 다른 문자열들이 계속 입력된다.
    temp.append(data[i])
ans = "".join(temp[:n - k])
print(ans)
