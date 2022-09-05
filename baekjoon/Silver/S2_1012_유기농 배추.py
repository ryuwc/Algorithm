import sys
sys.setrecursionlimit(10 ** 6)  # 일단 혹시 몰라 넣어줌

def dfs(N, M, r, c):        # 미로에서 dfs를 사용하는 것과 같이 재귀 dfs를 선언
    visited[r][c] = 1
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                dfs(N, M, nr, nc)


for tc in range(int(sys.stdin.readline())):
    N, M, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    for k in range(K):      # 좌표를 받아 1로 채움 == 미로와 같이
        r, c = map(int, sys.stdin.readline().split())
        arr[r][c] = 1

    visited = [[0]*M for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            # 중요! 영역의 갯수를 구하는 것이기에 visited가 0이라는 조건 필수로 걸어줘야됨
            if arr[i][j] == 1 and visited[i][j] == 0:
                dfs(N, M, i, j)
                result += 1

    print(result)