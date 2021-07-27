import sys

def tsp(last, visited):
    if visited == ALL_VISITED:
        return data[last][0] or float('inf')

    if dp[last][visited] != -1:
        return dp[last][visited]

    temp = float('inf')
    # 모든 도시를 확인 하는데 안에서 조건으로 걸러낸다.
    for next_city in range(n):
        # 비트 마스크로 출입을 확인하기 때문에 만약 도시가 0, 1, 2, 3인 것을
        # AND연산을 통해서 확인한다. -> 비트가 켜져있는지를 말하지 않고 그 비트의 값을 주기 떄문에
        # 1을 이용하려 하면 안 된다.
        if visited & (1 << next_city) == 0 and data[last][next_city] != 0:
            # OR연산으로 함수의 인자로 넘겨주기 때문에 현재 가지고 있는 visited는 변경이 생기지 않는다.
            temp = min(temp, tsp(next_city, visited | (1 << next_city)) + data[last][next_city])

    dp[last][visited] = temp
    return temp

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]
ALL_VISITED = (1 << n) - 1

print(tsp(0, 1 << 0))