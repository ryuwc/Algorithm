import collections, heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        # 정점: 인접정점, 가중치 딕셔너리 그래프 만들기
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])
        k = 0
        # 이 문제는 싸이클이 도는 그래프가 주어지기 때문에 시간초과남
        # visit으로 중복 방지 {노드: 움직인 거리}
        visit = {}
        Q = [(0, src, 0)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            # visit에 있어도 방문 해도 됨
            # 하지만, 그 거리가 현재 거리보다 더 크면 안됨, 비용은 이미 최소화 되있음
            if node not in visit or visit[node] > k:
                visit[node] = k
                for v, w in graph[node]:
                    if k <= K:
                        alt = price + w
                        heapq.heappush(Q, (alt, v, k + 1))
        return -1
