import heapq


class Solution(object):
    def swimInWater(self, grid):
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/mx-height, r, c)
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        # 다익스트라 알고리즘 사용
        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N-1 and c == N-1:
                return t

            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
