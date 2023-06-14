import sys

sys.setrecursionlimit(10 ** 6)

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(h, x, y):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] >= h and visited[nx][ny] == 0:
            dfs(h, nx, ny)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_safe_area = 0

for h in range(1, 101):
    visited = [[0] * N for _ in range(N)]
    safe_area_count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= h and visited[i][j] == 0:
                dfs(h, i, j)
                safe_area_count += 1
    max_safe_area = max(max_safe_area, safe_area_count)

print(max_safe_area)
