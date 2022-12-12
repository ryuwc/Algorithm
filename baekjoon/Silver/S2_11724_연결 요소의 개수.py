import sys; from collections import defaultdict
sys.setrecursionlimit(10 ** 6)


def dfs(v):
    if visit[v]:
        return

    visit[v] = 1

    for u in graph[v]:
        dfs(u)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = [0] * (N + 1)

    rst = 0
    for i in range(1, N + 1):
        if visit[i] == 0:
            dfs(i)
            rst += 1

    print(rst)
