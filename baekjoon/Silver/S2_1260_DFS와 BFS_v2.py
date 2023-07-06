import sys
from collections import defaultdict, deque


def dfs(u, G, visit, dfs_lst):
    if u in visit:
        return
    visit.add(u)
    dfs_lst.append(u)
    for v in sorted(G[u]):
        dfs(v, G, visit, dfs_lst)


def bfs(u, G, visit, bfs_lst):
    Q = deque()
    Q.append(u)
    visit.add(u)
    bfs_lst.append(u)
    while Q:
        v = Q.popleft()
        for u in sorted(G[v]):
            if u in visit:
                continue
            Q.append(u)
            visit.add(u)
            bfs_lst.append(u)


def main():
    N, M, V = map(int, sys.stdin.readline().strip().split())
    G = defaultdict(list)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        G[a].append(b)
        G[b].append(a)

    dfs_lst = []
    visit = set()
    dfs(V, G, visit, dfs_lst)
    bfs_lst = []
    visit = set()
    bfs(V, G, visit, bfs_lst)
    print(' '.join(map(str, dfs_lst)))
    print(*bfs_lst)


if __name__ == '__main__':
    main()
