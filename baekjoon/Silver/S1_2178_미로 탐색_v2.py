import sys
from collections import deque

def bfs(maze, start, visit):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([start])

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == 1 and not visit[nr][nc]:
                visit[nr][nc] = visit[r][c] + 1
                queue.append((nr, nc))

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    bfs(maze, (0, 0), visit)
    print(visit[N-1][M-1] + 1)

if __name__ == '__main__':
    main()
