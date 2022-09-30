import sys; sys.stdin = open('1249.txt')
from heapq import heappop, heappush

for tc in range(1, int(input())+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]

    # 다익스트라로 최단 거리 구하기
    visit = [[0]*N for _ in range(N)]
    D = [[0xffffff]*N for _ in range(N)]
    D[0][0] = 0

    # 우선순위큐를 사용하기 위해 heapq사용
    Q = []
    heappush(Q, (0, 0, 0))  # (거리, r, c)

    while Q:
        d, r, c = heappop(Q)
        # 방문 확인 작업
        if visit[r][c]: continue
        visit[r][c] = 1

        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and D[nr][nc]:
                # 간선 완화 작업
                if D[nr][nc] > D[r][c]+maps[nr][nc]:
                    D[nr][nc] = D[r][c] + maps[nr][nc]
                    heappush(Q, (D[nr][nc], nr, nc))

    print(f'#{tc}', D[N-1][N-1])
