from typing import List
from collections import deque

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        q = deque([])
        probaStore = [0] * n
        edge = dict()

        for item in range(n):
            edge[item] = []

        for idx, temp in enumerate(edges):
            a, b = temp
            edge[a].append((b, idx))
            edge[b].append((a, idx))

        probaStore[start] = 1
        q.append((start, probaStore[start]))
        while q:
            now_node, proba = q.popleft()

            if now_node == end:
                if proba > probaStore[now_node]:
                    probaStore[now_node] = proba
                    continue

            for next_node, idx in edge[now_node]:
                now_proba = probaStore[now_node] * succProb[idx]
                if now_proba > probaStore[next_node]:
                    probaStore[next_node] = now_proba
                    q.append((next_node, now_proba))
        return probaStore[end]

sol = Solution()
print(sol.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))