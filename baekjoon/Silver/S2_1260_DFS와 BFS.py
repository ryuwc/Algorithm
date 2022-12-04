import sys; from collections import defaultdict, deque

def dfs(u):
    global dfs_lst
    if u in visit_dfs:
        return
    dfs_lst.append(u)
    visit_dfs.add(u)
    for v in G[u]:
        dfs(v)

def bfs(u):
    global bfs_lst
    Q = deque()
    Q.append(u)
    visit_bfs.add(u)
    bfs_lst.append(u)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v not in visit_bfs:
                visit_bfs.add(v)
                bfs_lst.append(v)
                Q.append(v)


N, M, V = map(int, sys.stdin.readline().strip().split())
G = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    G[a].append(b)
    G[b].append(a)

for lst in G.values():
    lst.sort()

visit_dfs = set()
visit_bfs = set()
dfs_lst = []
bfs_lst = []
dfs(V)
bfs(V)
print(*dfs_lst)
print(*bfs_lst)

