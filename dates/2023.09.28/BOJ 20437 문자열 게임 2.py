import sys

t = int(sys.stdin.readline())

for _ in range(t):
    w = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())

    data = dict()
    for i in range(len(w)):
        char = w[i]
        if char not in data:
            data[char] = []
        data[char].append(i)

    min_val, max_val = float("inf"), -float("inf")
    for key in data.keys():
        temp_idxes = data[key]
        if len(temp_idxes) < k:
            continue

        for i in range(len(temp_idxes) - k + 1):
            value = temp_idxes[i + k - 1] - temp_idxes[i] + 1
            min_val = min(min_val, value)
            max_val = max(max_val, value)
    if min_val == float("inf"):
        print(-1)
    else:
        print(f"{min_val} {max_val}")
