import sys
sys.setrecursionlimit(10 ** 6)

def dfs(N, h, r, c):
    visited[r][c] = 1
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + di, c + dj
        if 0 <= nr < N and 0 <= nc < N:
            '''
            이 문제는 높이 h이상인 지역을 탐색해야한다.
            '''
            if arr[nr][nc] >= h and visited[nr][nc] == 0:
                dfs(N, h, nr, nc)

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]


result = 0
for k in range(1, 101):
    visited = [[0]*N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= k and visited[i][j] == 0:   # 높이 k이상인 지역을 탐색
                dfs(N, k, i, j)
                tmp += 1
    if tmp > result:
        result = tmp

print(result)