class Solution(object):

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        N = len(image)
        M = len(image[0])
        visit = [[0]*M for _ in range(N)]
        visit_color = image[sr][sc]
        def dfs(r, c):
            visit[r][c] = 1
            image[r][c] = color
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if visit[nr][nc] == 0 and image[nr][nc] == visit_color:
                        dfs(nr, nc)
        dfs(sr, sc)
        return image
