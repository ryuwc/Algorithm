class Solution(object):
    def pacificAtlantic(self, heights):
        N, M = len(heights), len(heights[0])
        # pac = Pacific Ocean으로 갈 수 있는 좌표, atl = Atlantic으로 갈 수 있는 좌표
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # 현재 위치가 visit에 있거나, 경계를 벗어나거나, 전의 위치보다 작으면 return
            if ((r, c) in visit or r < 0 or c < 0 or r == N or c == M or heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])


        # 2차원 배열의 각 테두리 부분 위치에서 dfs탐색 시작
        for i in range(M):
            dfs(0, i, pac, heights[0][i])
            dfs(N - 1, i, atl, heights[N-1][i])

        for r in range(N):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, M - 1, atl, heights[r][M-1])

        rst = []
        for r in range(N):
            for c in range(M):
                # (r, c)가 pac과 atl에 동시에 존재하면 그 좌표는 두 바다를 갈 수 있음
                if (r, c) in pac and (r, c) in atl:
                    rst.append([r, c])
        return rst
