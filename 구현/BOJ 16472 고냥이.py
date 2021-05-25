import sys

n = int(sys.stdin.readline())
data = list(sys.stdin.readline().strip())
alpha = [0] * 26
start, length, ans, cnt = 0, 1, 0, 1
alpha[ord(data[start]) - 97] += 1

for end in range(1, len(data)):
    idx = ord(data[end]) - 97

    if alpha[idx] == 0:
        cnt += 1
    length += 1
    alpha[idx] += 1

    if cnt <= n:
        ans = max(ans, length)
    else:
        while start < end and cnt > n:
            idx = ord(data[start]) - 97
            alpha[idx] -= 1
            start += 1
            length -= 1
            if alpha[idx] == 0:
                cnt -= 1
print(ans)