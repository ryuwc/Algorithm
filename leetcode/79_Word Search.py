from collections import defaultdict
class Solution(object):
    def exist(self, board, word):
        N, M = len(board), len(board[0])

        # dfs탐색 하기 전의 사전 작업 단어가 충분하지 않다면, 바로 False를 return
        charCount = defaultdict(lambda: 0)
        for i in range(len(board)):
            for j in range(len(board[0])):
                charCount[board[i][j]] += 1
        for ch in word:
            charCount[ch] -= 1
            if charCount[ch] < 0:
                return False

        # 중복 탐색 방지
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            # 위치가 범위를 벗어나거나, 현재 위치의 단어가 word의 i번째와 다르르거나, 이미 방문 했었으면 return
            if (r < 0 or c < 0 or
                r >= N or c >= M or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            # 4방향에 대해 dfs 탐색, 한 개라도 True가 나오면 True를 리턴
            rst = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r, c))
            return rst

        for i in range(N):
            for j in range(M):
                if dfs(i, j, 0):
                    return True
        return False