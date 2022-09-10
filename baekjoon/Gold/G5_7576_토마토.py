import sys
from collections import deque

def bfs(N, M):          # 여러개의 시작점을 갖는 bfs, 시작점에서의 거리를 탐색하며 알아냄
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                Q.append((i, j))

    while Q:
        i, j = Q.popleft()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nr, nc = i + di, j + dj
            if 0 <= nr < N and 0 <= nc < M:
                if tomato[nr][nc] == 0 and visited[nr][nc] == 0:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[i][j] + 1

def result(N, M):           # 안익은 토마토가 있는지 확인하는 함수
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                if visited[i][j] == 0:
                    return print(-1)
    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] > ans:
                ans = visited[i][j]
    return print(ans)

M, N = map(int, sys.stdin.readline().split())

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

Q = deque()
visited = [[0]*M for _ in range(N)]
bfs(N, M)

result(N, M)

# for line in visited:
#     print(*line)
