
N = int(input())
T_N = int(input())

record = [[0] * N for _ in range(N)]

sr, sc = 0, 0

D = [[1, 0], [0, 1], [-1, 0], [0, -1]]

record[0][0] = N*N
cnt = (N*N)-1
k = 0



while cnt > 0:
    nr, nc = sr + D[k][0], sc + D[k][1]
    if 0 <= nr < N and 0 <= nc < N and record[nr][nc] == 0:
        record[nr][nc] = cnt
        cnt -= 1
        sr, sc = nr, nc
    else:
        k = (k+1)%4

tr, tc = 0, 0
for i in range(N):
    for j in range(N):
        if record[i][j] == T_N:
            tr = i
            tc = j
            break

for line in record:
    print(*line)

print(tr+1, tc+1)