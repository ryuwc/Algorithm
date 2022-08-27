import sys; sys.stdin = open('4875.txt', 'r')

def dfs(vr, vc):
    visited[vr][vc] = 1
    dr = [0, 1, 0, -1]      # 우, 하, 좌, 상
    dc = [1, 0, -1, 0]
    for w in G[vr][vc]:     # w는 갈 수 있는 방향의 값이 들어있을 것.
        nr = vr + dr[w]
        nc = vc + dc[w]
        if visited[nr][nc] == 0:
            dfs(nr, nc)

for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    dr = [0, 1, 0, -1]  # 우, 하, 좌, 상
    dc = [1, 0, -1, 0]

    visited = [[0]*N for _ in range(N)]

    G = [[[] for a in range(N)] for d in range(N)]      # 연결 리스트를 3차원 리스트로 생성
    for k in range(4):              # 연결 리스트에 4방향의 delta를 넣어준다.
        for i in range(N):
            for j in range(N):
                nr = i + dr[k]
                nc = j + dc[k]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if maze[i][j] == 1:
                    continue
                elif maze[nr][nc] == 0 or maze[nr][nc] == 2:
                    G[i][j].append(k)


    vr, vc = 0, 0           # 출발점
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                vr, vc = i, j

    final_r = 0
    final_c = 0
    for i in range(N):      # 종료점
        for j in range(N):
            if maze[i][j] == 2:
                final_r, final_c = i, j
    # print(G)
    dfs(vr, vc)

    if visited[final_r][final_c] == 1:  # 종료점의 visited에 1이 있다면 들린 것이므로 1을 출력
        print(f'#{tc+1}', 1)
    else:
        print(f'#{tc+1}', 0)

