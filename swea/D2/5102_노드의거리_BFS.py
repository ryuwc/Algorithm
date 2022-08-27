# 노드의 거리
import sys; sys.stdin = open('5102.txt', 'r')

def bfs(v):
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                visited[w] = 1
                Q.append(w)
                D[w] = D[v] + 1
                P[w] = v


for tc in range(int(input())):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    s, g = map(int, input().split())
    Q = []
    visited = [0] * 51
    D = [0] * (V + 1)
    P = [0] * (V + 1)

    bfs(s)
    print(f'#{tc+1}', D[g])
