class Solution(object):
    def longestIncreasingPath(self, matrix):
        N, M = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, preVal):
            if (r < 0 or c < 0 or r == N or c == M or matrix[r][c] <= preVal):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            rst = 1
            rst = max(rst, 1 + dfs(r+1, c, matrix[r][c]))
            rst = max(rst, 1 + dfs(r-1, c, matrix[r][c]))
            rst = max(rst, 1 + dfs(r, c+1, matrix[r][c]))
            rst = max(rst, 1 + dfs(r, c-1, matrix[r][c]))
            dp[(r, c)] = rst
            return rst

        for i in range(N):
            for j in range(M):
                dfs(i, j, -1)

        return max(dp.values())