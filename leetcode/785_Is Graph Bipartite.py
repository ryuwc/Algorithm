
class Solution(object):
    def isBipartite(self, graph):
        # graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        """
        :type graph: List[List[int]]
        :rtype
        """
        N = len(graph)
        seen = set()
        colors = [0] * N
        def dfs(r, c):
            for start_idx in range(N):
                if start_idx in seen: continue
                stack = []
                stack.append(start_idx)
                colors[start_idx] = 1

                while stack:
                    idx = stack.pop()
                    conn_idxs = graph[idx]
                    color = colors[idx]

                    for conn_idx in conn_idxs:
                        if conn_idx not in seen:
                            seen.add(conn_idx)
                            stack.append(conn_idx)
                            colors[conn_idx] = -1 * color
                            continue
                        if colors[conn_idx] * colors != -1:
                            return False

                    return True
            return dfs(r, c)



