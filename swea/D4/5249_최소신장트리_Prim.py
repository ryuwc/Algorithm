import sys; sys.stdin = open('5249.txt', 'r')

def prim(r, V):
    MST = [0] * (V+1)
    key = [1e9] * (V+1)
    key[r] = 0
    for _ in range(V):
        u, w = 0, 1e9
        for i in range(V+1):
            if MST[i]==0 and key[i] < w:
                u, w = i, key[i]
        MST[u] = 1
        for v in range(V+1):
            if MST[v]==0 and G[u][v] > 0:
                key[v] = min(key[v], G[u][v])
    return sum(key)

for tc in range(int(input())):
    V, E = map(int, input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        u, v, weight = map(int, input().split())
        G[u][v] = weight
        G[v][u] = weight

    # for line in G:
    #     print(line)
    print(f'#{tc+1}', prim(0, V))