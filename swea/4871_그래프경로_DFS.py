import sys; sys.stdin = open('4871.txt', 'r')


def dfs(v):                 # dfs 함수 선언
    visited[v] = 1          # visited에 다녀간 흔적을 1으로 남겨둠
    for w in G[v]:          # v에 연결된 값들을 반복문으로 돌림
        if visited[w] == 0: # w에 방문하지 않았다면
            dfs(w)          # 재귀
# 재귀가 다 되면(함수가 끝나면) visited에는 지나온 흔적이 남겨져 있을 것이다.


for tc in range(int(input())):
    V, E = map(int, input().split())     # V개의 노드, E개의 간선
    G = [[] for _ in range(V + 1)]       # 노드의 수 만큼 인접리스트를 생성
    for _ in range(E):
        u, v = map(int, input().split()) # u정점의 인접 정점 v
        G[u].append(v)                   # 인접리스트에 넣어줌, 간선이 아니라면 G[v].append(u)도 해줘야됨
    s, g = map(int, input().split())     # 시작 정점, 도착 정점
    visited = [0] * 51
    dfs(s)
    if visited[g] == 1:                  # 도착 정점이 visited에 기록되어 있다면
        print(f'#{tc+1}', 1)             # 1을 출력
    else:
        print(f'#{tc+1}', 0)





