def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    n = len(edges)
    par = [i for i in range(n + 1)]

    def find(n):
        p = par[n]
        while par[p] != p:
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return False
        par[p2] = p1
        return True

    for a, b in edges:
        if not union(a, b):
            return [a, b]