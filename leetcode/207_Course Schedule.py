import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문했던 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True
