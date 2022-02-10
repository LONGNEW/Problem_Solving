import sys
from collections import deque

def find(node, value):
    if node == parent[node]:
        return
    ids[parent[node]] = value
    find(parent[node], value)

def bfs(ins_id):
    q = deque([ins_id])

    while q:
        node = q.popleft()

        if node not in graph:
            continue

        for next_node in graph[node]:
            ids[next_node] = ids[ins_id]
            q.append(next_node)

n = int(sys.stdin.readline())

# ids는 실제 개체의 식별 번호를 저장하기 위함.
# graph에는 이미 죽은 개체가 들어 있을 수 있음
# BFS 구현 시에 주의 필요
graph, dead, ids, parent = dict(), [], dict(), dict()

idx = 1
for _ in range(n):
    temp = sys.stdin.readline().rstrip()

    if temp == "F":
        graph[idx] = []

    parent[idx] = idx
    ids[idx] = -idx
    idx += 1

m = int(sys.stdin.readline())
for _ in range(m):
    temp = list(sys.stdin.readline().split())

    if len(temp) == 1:
        dead.append(-int(temp[0]))
    else:
        m = int(temp[1])
        if temp[2] == "F":
            graph[idx] = []

        graph[m].append(idx)

        parent[idx] = m
        ids[idx] = -idx
        idx += 1

k = int(sys.stdin.readline())
for _ in range(k):
    # female인지 확인 -> graph 딕셔너리에 id 존재하는지
    dna_id, dna_num = map(int, sys.stdin.readline().split())
    ids[dna_id] = dna_num

    if dna_id in graph:
        bfs(dna_id)
    find(dna_id, dna_num)

for key in graph.keys():
    if parent[key] == key:
        bfs(key)

for item in dead:
    del ids[item]

f_temp, m_temp = set(), set()
for key in ids.keys():
    if key in graph:
        f_temp.add(ids[key])
    else:
        m_temp.add(ids[key])

cnt = 0
for item in f_temp:
    if item > 0:
        cnt += 1

if cnt > 1 and len(f_temp) > 1:
    print("NO")
    exit(0)

cnt = 0
for item in m_temp:
    if item > 0:
        cnt += 1

    if cnt >= 2:
        print("NO")
        exit(0)

ans = f_temp.union(m_temp)

print("YES" if len(ans) == 1 else "POSSIBLY")