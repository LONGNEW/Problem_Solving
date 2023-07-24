def solution(numbers):
    targets = set()

    def factorial(data, used, string):
        if len(string) > 0:
            targets.add(int(string))
        for key in data.keys():
            if data[key] == used[key]:
                continue
            used[key] += 1
            factorial(data, used, string + key)
            used[key] -= 1

    data, used = dict(), dict()
    for item in numbers:
        if item not in data:
            data[item] = 0
            used[item] = 0
        data[item] += 1
    factorial(data, used, "")

    data = list(targets)
    cnt = 0
    for item in data:
        if item < 2:
            continue

        flag = 1
        for comp in range(2, int(item ** (1 / 2) + 1)):
            if item % comp == 0:
                flag = 0
                break

        if flag:
            cnt += 1
    return cnt