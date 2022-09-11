import sys
sys.setrecursionlimit(10 ** 6)


def dfs(r, c, N, M):    # 단지번호붙이기와 비슷하다
    global ret
    ret += 1            # 면적을 더해주는 변수
    visited[r][c] = 1
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + di, c + dj
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0 and visited[nr][nc] == 0:  # 이 문제는 arr가 0일 때를 탐색해야한다.
                dfs(nr, nc, N, M)


N, M, K = map(int, sys.stdin.readline().split())

arr = [[0]*M for _ in range(N)]

for k in range(K):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

visited = [[0]*M for _ in range(N)]

total = 0
ret = 0
ret_lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            dfs(i, j, N, M)
            total += 1
            ret_lst.append(ret)
            ret = 0
ret_lst.sort()

print(total)
print(*ret_lst)