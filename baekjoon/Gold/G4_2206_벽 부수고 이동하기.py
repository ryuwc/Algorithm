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
                elif maze[nr][nc] == 1 and z == 0:                  # 벽이고 벽을 부술 수 있으면
                    visited[nr][nc][z+1] = visited[r][c][z] + 1
                    Q.append((nr, nc, z+1))
    return -1
N, M = map(int, sys.stdin.readline().split())

maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

Q = deque()
'''
visited를 만들 때 3차원으로 만들어, 벽을 부순 횟수를 기록한다.
visited[r][c][z] = [0, 0]인데, z가 0이면 벽을 부수지 않은 상태, 1이면 벽을 부순 상태이다.
즉, visited[r][c][z]의 첫 번째 인덱스는 벽을 부수지 않은 상태에서의 최단 거리, 두 번째 인덱스는 벽을 부순 상태에서의 최단 거리이다.
'''
visited = [[[0] * 2 for _ in range(M)]for _ in range(N)]


print(bfs2())


