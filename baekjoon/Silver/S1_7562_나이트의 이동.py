import sys
from collections import deque
# sys.stdin = open('S1_7562_나이트의 이동.txt', 'r')
sys.setrecursionlimit(10**6)

# 나이트가 갈 수 있는 방향
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

def solve(r, c, er, ec):
    global cnt, visit, Q, record
    # 현재 위치 방문 체크
    visit.add((r, c))
    Q.append((r, c))
    while Q:
        r, c = Q.popleft()
        # 목표 위치에 도달하면 적어뒀던 거리를 반환하고 함수 종료
        if r == er and c == ec:
            return record[er][ec]
        for k in range(8):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visit:
                # record는 출발지로부터의 거리를 저장함
                record[nr][nc] = record[r][c] + 1
                Q.append((nr, nc))
                visit.add((nr, nc))
    # 도달하지 못했다면 0을 반환
    return 0

for tc in range(int(sys.stdin.readline().strip())):
    N = int(sys.stdin.readline().strip())

    sr, sc = map(int, sys.stdin.readline().strip().split())
    er, ec = map(int, sys.stdin.readline().strip().split())

    Q = deque()
    visit = set()
    record = [[0] * N for _ in range(N)]

    print(solve(sr, sc, er, ec))

