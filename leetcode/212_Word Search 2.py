class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution(object):
    def findWords(self, board, words):
        root = TrieNode()

        for w in words:
            root.addWord(w)

        N, M = len(board), len(board[0])
        rst, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == N or c == M or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                rst.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visit.remove((r, c))
        for r in range(N):
            for c in range(M):
                dfs(r, c, root, "")

        return list(rst)