import sys; sys.stdin = open('불.txt', 'r')
# import sys; sys.stdin = open('불 - 복사본.txt', 'r')
from collections import deque

# 불이 퍼지는 함수 시간 단위로 한번만 실행됨
def bfs1():
    for _ in range(len(Q_f)):
        r, c = Q_f.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == '.' or arr[nr][nc] == '@':
                    arr[nr][nc] = '*'
                    Q_f.append((nr, nc))

# 움직이는 함수, 갈수 있는 방향에서 한번 움직이고 불 함수를 호출
# 불 - 이동 - 불 - 이동 순서
def bfs2(r, c):
    visited[r][c] = 1
    while Q_p:
        for _ in range(len(Q_p)):
            r, c = Q_p.popleft()
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r + di, c + dj
                if not (0 <= nr < N and 0 <= nc < M):
                    return visited[r][c]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == '.':
                    visited[nr][nc] = visited[r][c] + 1
                    Q_p.append((nr, nc))
        bfs1()
    return 'IMPOSSIBLE'

for tc in range(int(input())):
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    Q_f = deque()
    Q_p = deque()
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '@':
                Q_p.append((i, j))
            elif arr[i][j] == '*':
                Q_f.append((i, j))

    bfs1()
    r, c = Q_p[0]
    print(bfs2(r, c))
    # for line in visited:
    #     print(*line)
    # print('=====================================')