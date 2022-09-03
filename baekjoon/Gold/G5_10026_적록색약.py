import sys
sys.setrecursionlimit(10 ** 6)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(color, N, r, c):
    visited[r][c] = 1
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == color and visited[nr][nc] == 0:
                dfs(color, N, nr, nc)


N = int(sys.stdin.readline())
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]

color = ['R', 'G', 'B']

result_1 = 0

for c in color:
    for i in range(N):
        for j in range(N):
            if arr[i][j] == c and not visited[i][j]:
                dfs(c, N, i, j)
                result_1 += 1

color = ['R', 'B']
visited = [[0]*N for _ in range(N)]
result_2 = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for c in color:
    for i in range(N):
        for j in range(N):
            if arr[i][j] == c and not visited[i][j]:
                dfs(c, N, i, j)
                result_2 += 1

print(result_1, result_2)
