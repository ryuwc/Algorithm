import sys; from collections import deque

def solve(i, j, who):
    cnt = 0
    Q = deque()
    Q.append((i, j))
    visit.add((i, j))
    cnt += 1
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visit and arr[nr][nc] == who:
                cnt += 1
                Q.append((nr, nc))
                visit.add((nr, nc))
    return cnt

M, N = map(int, sys.stdin.readline().strip().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(N)]

visit = set()

rst = [0, 0]

for i in range(N):
    for j in range(M):
        if (i, j) not in visit:
            val = solve(i, j, arr[i][j]) ** 2
            if arr[i][j] == 'W':
                rst[0] = rst[0] + val
            elif arr[i][j] == 'B':
                rst[1] = rst[1] + val

print(*rst)

