import sys
from collections import deque
sys.setrecursionlimit(10**6)

# 나이트가 갈 수 있는 방향
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

def solve(N, sr, sc):
    visit = set()
    record = [[0] * N for _ in range(N)]
    Q = deque([(sr, sc)])
    visit.add((sr, sc))

    while Q:
        r, c = Q.popleft()
        for k in range(8):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visit:
                record[nr][nc] = record[r][c] + 1
                Q.append((nr, nc))
                visit.add((nr, nc))
    return record

for tc in range(int(sys.stdin.readline().strip())):
    N = int(sys.stdin.readline().strip())
    sr, sc = map(int, sys.stdin.readline().strip().split())
    er, ec = map(int, sys.stdin.readline().strip().split())

    record = solve(N, sr, sc)
    print(record[er][ec])
