import sys; sys.stdin = open('1249.txt')


for tc in range(1, int(input())+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]

    #BFS로 최단 거리 구하기
    D = [[0xffffff]*N for _ in range(N)]
    D[0][0] = 0
    Q = [(0, 0)]

    while Q:
        r, c = Q.pop(0)
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and D[nr][nc] > D[r][c]+maps[nr][nc]:
                D[nr][nc] = D[r][c] + maps[nr][nc]
                Q.append((nr, nc))

    print(f'#{tc}', D[N-1][N-1])


