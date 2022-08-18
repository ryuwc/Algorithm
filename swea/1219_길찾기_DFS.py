import sys; sys.stdin = open('1219.txt', 'r')

def dfs(v):
    visited[v] = 1
    for w in G[v]:
        if visited[w] == 0:
            dfs(w)

for _ in range(1, 11):
    tc, V = map(int, input().split())
    G = [[] for _ in range(100)]
    visited = [0]*101
    road = list(map(int, input().split()))
    u = []
    v = []
    for i in range(len(road)):   # 인덱스가 짝수면 u리스트에 넣어주고
        if i % 2 == 0:           # 홀수면 v에 넣어준다
            u.append(road[i])
        else:
            v.append(road[i])
    for i in range(len(u)):      # G라는 빈 2차원 리스트에 넣어주는 방법
        G[u[i]] += [v[i]]
    dfs(0)
    if visited[99] == 1:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
