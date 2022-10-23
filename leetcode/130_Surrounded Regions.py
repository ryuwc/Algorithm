class Solution(object):
    def solve(self, board):
        N, M = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == N or c == M or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # 1. X로 둘려 쌓여 있지 않은 O를 캡처 (O -> T)로 변경 (테두리에 있는 O)
        for i in range(N):
            for j in range(M):
                if board[i][j] == "O" and (i in [0, N-1] or j in [0, M-1]):
                    dfs(i, j)

        # 2. X로 둘려 쌓여 있는 O를 X로 변경
        for i in range(N):
            for j in range(M):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # 3. T로 변경한 값을 O로 바꾸기
        for i in range(N):
            for j in range(M):
                if board[i][j] == "T":
                    board[i][j] = "O"

