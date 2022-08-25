import sys; sys.stdin = open('input_미로1.txt', 'r')

def bfs(r, c):
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        r, c = Q.pop(0)
        if maze[r][c] == 3:
            return 1
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if maze[nr][nc] != 1 and visited[nr][nc] == 0 and 0 <= nr < 16 and 0 <= nc < 16:
                Q.append((nr, nc))
                visited[nr][nc] = 1
    return 0

for y in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    Q = []

    sr, sc, er, ec = 0, 0, 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sr, sc = i, j
            elif maze[i][j] == 3:
                er, ec = i, j

    print(f'#{tc}', bfs(sr, sc))
