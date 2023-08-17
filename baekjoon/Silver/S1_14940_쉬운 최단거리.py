import sys
from collections import deque

sinput = sys.stdin.readline


def find_two(N, M, maps):
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                return i, j


def main():
    N, M = map(int, sinput().rstrip().split())
    maps = [list(map(int, sinput().rstrip().split())) for _ in range(N)]

    er, ec = find_two(N, M, maps)
    maps[er][ec] = 0
    Q = deque([(er, ec)])
    visit = [[-1] * M for _ in range(N)]
    visit[er][ec] = 0

    while Q:
        r, c = Q.popleft()
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == -1:
                if maps[nr][nc] == 0:
                    visit[nr][nc] = 0
                else:
                    visit[nr][nc] = visit[r][c] + 1
                    Q.append((nr, nc))

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                print(0, end=' ')
            else:
                print(visit[i][j], end=' ')
        print()


main()
