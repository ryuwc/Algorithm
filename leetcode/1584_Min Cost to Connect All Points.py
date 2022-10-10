import heapq


class Solution(object):
    def minCostConnectPoints(self, points):
        N = len(points)

        adj = { i:[] for i in range(N) }  # i : [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # 프림 알고리즘
        rst = 0
        visit = set()
        # 0에서 출발, 0에서 0으로 가는 비용은 0임
        minH = [[0, 0]] # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            rst += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return rst
