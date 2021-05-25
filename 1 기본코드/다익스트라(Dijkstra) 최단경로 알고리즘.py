import sys
import heapq
INF = 1000000

n , e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
# 이 distance 배열의 경우엔 dijkstra 함수 안에서 초기화를 시켜서
# 리턴을 하는 방법을 이용할 수도 있다.
# 각 노드에 대한 최단 거리를 기록하는 방법도 존재.
distance = [INF] * (n + 1)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now_node = heapq.heappop(q)
        # 경로의 비용이 커서 계속 뒤에 남아있다가 마지막에
        # 들어오는 경우를 걸러내기 위함.
        # visit의 역할도 하는듯 이미 최단 경로가 들어와 있으면
        # 아래의 반복문이 실행될 이유가 없으니.
        if distance[now_node] < dist:
            continue
        for next_dis, next_node in graph[now_node]:
            cost = dist + next_dis
            if distance[next_node] > cost:
                distance[next_node] = cost
                # 현재에서 이동한 다음 노드까지 의 경로는
                # 총합 경로이기에 더한 값이 들어가야 한다.
                heapq.heappush(q, (cost, next_dis))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])