import sys; from collections import deque

def bfs(H, N, M):
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[h][i][j] == 1:
                    Q.append((h, i, j))
                    visited[h][i][j] = 1
    while Q:
        h, i, j = Q.popleft()
        '''
        3차원 리스트에서의 움직임의 델타를 추가하면 된다.
        2차원의 델타가 [1, 0].. 이었다면, 
        3차원은 [1, 0, 0], [0, 0, 1]... 등으로 주면 된다.
        '''
        for dh, di, dj in [[1, 0, 0], [0, 0, 1], [-1, 0, 0], [0, 0, -1], [0, 1, 0], [0, -1, 0]]:
            nh, nr, nc = h + dh, i + di, j + dj
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                if tomato[nh][nr][nc] == 0 and visited[nh][nr][nc] == 0:
                    Q.append((nh, nr, nc))
                    visited[nh][nr][nc] = visited[h][i][j] + 1

def result():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[h][i][j] == 0:
                    if visited[h][i][j] == 0:
                        return print(-1)
    ret = 0
    for h in range(H):
        for i in range(N):
            if max(visited[h][i]) > ret:
                ret = max(visited[h][i])
    return print(ret-1)

M, N, H = map(int, sys.stdin.readline().split())

tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for h in range(H)]

Q = deque()

visited = [[[0] * M for _ in range(N)]for h in range(H)]

bfs(H, N, M)

result()
