import collections
import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # [(소요시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            # heappop을 통해 가장 time이 적은 노드를 꺼내옴
            time, node = heapq.heappop(Q)
            # 그 노드가 dist(거리 정보)에 없다면 추가
            if node not in dist:
                dist[node] = time
                # 현재 노드의 인접 정점과 가중치를 Q에 추가
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        if len(dist) == n:
            return max(dist.values())
        return -1
