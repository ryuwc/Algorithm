class Solution(object):
    def findRedundantConnection(self, edges):

        n = len(edges)
        # 부모 초기화
        par = [i for i in range(n + 1)]

        def find(n):
            while par[n] != n:
                n = par[n]
            return n
        # n1과 n2의 부모가 같다면 합치지 않고 False를 return (부모가 같은 노드를 합치면 싸이클이 형성된다)
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            par[p2] = p1
            return True

        # 부모가 같은 노드를 발견 == 싸이클이 되므로 False가 return됨
        for a, b in edges:
            if not union(a, b):
                return [a, b]