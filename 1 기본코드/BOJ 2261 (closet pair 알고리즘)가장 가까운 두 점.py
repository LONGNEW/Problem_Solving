import sys


def dist(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def closest_pair(start, end):
    length = end - start
    if length == 2:
        return dist(position[start], position[start + 1])
    if length == 3:
        return min(dist(position[start], position[start + 1]), dist(position[start + 1], position[start + 2]), dist(position[start], position[start + 2]))

    mid = (start + end) // 2
    # 중간에 위치하는 x좌표를 찾기 위함.
    mid_pos = position[mid][0]
    # 그 x 좌표를 기준으로 왼쪽과 오른쪽에서 최소한의 거리를 이루는 지점을 찾음
    d = min(closest_pair(start, mid), closest_pair(mid, end))

    # d 거리 안에 존재하는 점들을 걸러냄.
    temp = []
    for i in range(start, end):
        if (mid_pos - position[i][0]) ** 2 <= d:
            temp.append(position[i])

    # y 좌표를 기준으로 정렬.
    temp.sort(key=lambda x:x[1])

    temp_d = d
    temp_len = len(temp)
    for i in range(temp_len - 1):
        for j in range(i + 1, temp_len):
            if (temp[i][1] - temp[j][1]) ** 2 > temp_d:
                break
            if (temp[i][1] - temp[j][1]) ** 2 < temp_d:
                d = min(d, dist(temp[i], temp[j]))
    return d


n = int(sys.stdin.readline())
pos = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    pos.append((x, y))

temp_pos = set(pos)
position = list(temp_pos)

if len(pos) != len(position):
    print(0)
else:
    position.sort()
    d = closest_pair(0, len(pos))
    print(d)