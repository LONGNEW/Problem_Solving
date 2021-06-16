import sys

print("거스름돈을 입력해 주세요 :", end=" ")
total = int(sys.stdin.readline())

print("가진 동전의 갯수를 입력해주세요 :", end=" ")
data = list(map(int, sys.stdin.readline().split()))

for idx, coin in enumerate([500, 100, 50, 10]):
    total += data[idx] * coin

ans = []
for coin in [500, 100, 50, 10]:
    ans.append(total // coin)
    total %= coin

for idx, coin in enumerate([500, 100, 50, 10]):
    print(coin, "동전", ans[idx], "개")

print("환전 후 가지고 있는 동전의 개수 :", sum(ans))
