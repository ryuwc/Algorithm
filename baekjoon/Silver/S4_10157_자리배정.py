

R, C = map(int, input().split())
arr = [[0]*R for _ in range(C)]
K = int(input())

if K > R*C:
    print(0)
    exit()

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r = C -1
c = 0
arr[r][c] = 1
cnt = 0
k = 0
while arr[r][c] != K:
    nr, nc = r + dr[k], c + dc[k]
    if 0 <= nr < C and 0 <= nc < R and arr[nr][nc] == 0:
        arr[nr][nc] = arr[r][c] + 1
        r , c = nr, nc
    else:
        k = (k+1)%4
    cnt += 1

print(c+1, C-r)
for line in arr:
    print(*line)

