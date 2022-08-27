import sys; sys.stdin = open('5105.txt', 'r')

def bfs(r, c, N):
    visited = [[0]*N for _ in range(N)]
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        r, c = Q.pop(0)
        if maze[r][c] == 3:
            return print(visited[r][c]-2)
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and  0 <= nc < N and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return print(0)

for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    Q = []

    sr, sc = 0, 0
    er, ec = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
            elif maze[i][j] == 3:
                er, ec = i, j
    print(f'#{tc+1}', end=' ')
    bfs(sr, sc, N)
