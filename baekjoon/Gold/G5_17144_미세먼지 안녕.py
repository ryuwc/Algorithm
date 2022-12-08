import sys;
from collections import deque

# 먼지 확산 함수
def spread():
    # 먼지 담기
    munji = deque()
    for i in range(N):
        for j in range(M):
            if room[i][j] >= 1:
                munji.append((i, j, room[i][j]))

    # 먼지 확산
    while munji:
        r, c, amount = munji.popleft()
        d_count = 0
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != -1:
                d_count += 1
                room[nr][nc] += int(amount // 5)
        room[r][c] -= int(amount // 5) * d_count

def clean():
    # 위쪽 공기청정기
    r, c = cleaner[0][0], cleaner[0][1]
    # pre는 다음 칸에 넣을 값을 저장
    pre = 0
    for di, dj in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
        while True:
            nr, nc = r + di, c + dj
            if not (0 <= nr < N and 0 <= nc < M) or (room[nr][nc] == -1): break
            tmp = room[nr][nc]
            # 다음 칸에 pre를 넣고 pre는 현재 칸의 값을 저장
            room[nr][nc] = pre
            pre = tmp
            r = nr
            c = nc

    # 아래쪽 공기청정기
    r, c = cleaner[1][0], cleaner[1][1]
    pre = 0
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        while True:
            nr, nc = r + di, c + dj
            if not (0 <= nr < N and 0 <= nc < M) or (room[nr][nc] == -1): break
            tmp = room[nr][nc]
            room[nr][nc] = pre
            pre = tmp
            r = nr
            c = nc


if __name__ == '__main__':
    N, M, T = map(int, sys.stdin.readline().strip().split())
    room = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    cleaner = []
    for i in range(N):
        for j in range(M):
            if room[i][j] == -1:
                cleaner.append((i, j))


    for _ in range(T):
        spread()
        clean()

    rst = sum(map(sum, room)) + 2
    print(rst)
