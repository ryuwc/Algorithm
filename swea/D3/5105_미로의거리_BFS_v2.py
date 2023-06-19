from collections import deque


def bfs(sr, sc, maze, N):
    visited = [[0] * N for _ in range(N)]
    queue = deque([(sr, sc)])
    visited[sr][sc] = 1
    while queue:
        r, c = queue.popleft()
        if maze[r][c] == 3:
            return visited[r][c] - 2
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return 0


def main():
    for tc in range(int(input())):
        N = int(input())
        maze = [list(map(int, input())) for _ in range(N)]

        sr, sc = 0, 0
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    sr, sc = i, j
        print(f'#{tc + 1} {bfs(sr, sc, maze, N)}')


if __name__ == '__main__':
    main()
