import sys

# 북동남서
D = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
for_fir_dir = [1, 0, 3, 2]

visited = [[0] * M for _ in range(N)]
visited[r][c] = 1
cnt = 0
turn_cnt = 0
while True:
    d = (d-1)%4
    nr, nc = r + D[d][0], c + D[d][1]
    if arr[nr][nc] == 0 and visited[nr][nc] == 0:
        visited[nr][nc] = 1
        r, c = nr, nc
        turn_cnt = 0
        cnt += 1
    else:
        turn_cnt += 1
        if turn_cnt == 4:
            r = r - D[d][0]
            c = c - D[d][1]
            if arr[r][c] == 1:
                break
            else:
                turn_cnt = 0

print(cnt+1)

