import sys; from collections import deque

def bfs2():
    Q.append((0, 0, 0))
    visited[0][0][0] = 1
    while Q:
        r, c, z = Q.popleft()

        if r == N-1 and c == M-1:       # 도착지점에 도달하면 return
            return visited[r][c][z]

        for di, dj in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M:
                if maze[nr][nc] == 0 and visited[nr][nc][z] == 0:   # 벽이 아니고 방문하지 않았으면
                    visited[nr][nc][z] = visited[r][c][z] + 1
                    Q.append((nr, nc, z))
                # 기존 코드에서 이 부분만 수정하면된다.
                # 벽이고, z가 K보다 작고, visited의 z+1을 방문 하지 않았으면
                elif maze[nr][nc] == 1 and z < K and visited[nr][nc][z+1] == 0:
                    visited[nr][nc][z+1] = visited[r][c][z] + 1
                    Q.append((nr, nc, z+1))
    return -1

N, M, K = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
Q = deque()

# visited의 3차원 배열을 K+1 만큼 곱해준다.
visited = [[[0] * (K+1) for _ in range(M)]for _ in range(N)]

print(bfs2())