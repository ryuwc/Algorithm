import sys
from collections import deque
def bfs(r, c):
    Q = deque()
    Q.append((r, c))
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M:
                if maze[nr][nc] == 1 and visit[nr][nc] == 0:
                    visit[nr][nc] = visit[r][c] + 1
                    Q.append((nr, nc))

N, M = map(int, sys.stdin.readline().strip().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visit = [[0]*M for _ in range(N)]

bfs(0, 0)
print(visit[N-1][M-1]+1)